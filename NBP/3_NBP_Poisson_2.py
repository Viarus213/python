import numpy as np

# Poisson distriburion number generator
def PoissGen(l):
    P = S = 1
    q = np.exp(-l)

    while S > q:
        U = np.random.normal(0, 1)
        S = S * U
        P = P + 1
    return P


# Benford's Law number generator
def BenfordGen(n):
    P = S = 1
    q = np.log10(1 + 1 / n)

    while S > q:
        U = np.random.normal(0, 1)
        S = S * U
        P = P + 1
    return P


# Normal distribution numbers
def NormalGen():
    P = np.random.randint(0, 9)
    return P


POISSON_DISTRIBUTION = 0
NORMAL_DISTRIBUTION = 1
BENFORDS_LAW = 2

NoOfClients = 1500  # No. of clients
NoOfShops = 50  # No. of shops

DistName = ["* Poisson Distribution", "* Normal Distribution", "* Benford's Law"]

for DistType in range(3):
    print(DistName[DistType])

    for ExpectedVal in range(10):
        AllShopGainTab = NoOfShops * [0]
        AllClientsGainTab = NoOfClients * [0]

        for ShopNo in range(NoOfShops):

            for ClientNo in range(NoOfClients):
                BoughtProducts = PoissGen(ExpectedVal + 1)  # No. of promoted products
                BoughtProductsVal = BoughtProducts * 9  # Bought products price

                # Only promoted products
                if DistType == POISSON_DISTRIBUTION:
                    BoughtProductsVal = BoughtProductsVal
                # Promoted products + normal price products (Normal distribution)
                elif DistType == NORMAL_DISTRIBUTION:
                    BoughtProductsVal += NormalGen()
                # Promoted products + normal price products (Benfors's law)
                elif DistType == BENFORDS_LAW:
                    BoughtProductsVal += BenfordGen(ExpectedVal + 1)

                # Product values 1, 2, 6, 7 -> profit for client
                if (BoughtProductsVal % 5) <= 2:
                    AllClientsGainTab[ClientNo] += BoughtProductsVal % 5
                    AllShopGainTab[ShopNo] -= BoughtProductsVal % 5
                # Product values 3, 4, 8, 9 -> profit for shop
                elif (BoughtProductsVal % 5) >= 3:
                    AllShopGainTab[ShopNo] += 5 - (BoughtProductsVal % 5)
                    AllClientsGainTab[ClientNo] -= 5 - (BoughtProductsVal % 5)

        print("** Expected Value: ", ExpectedVal + 1)
        print("   Max Client Profit: ", max(AllClientsGainTab))
        print("   Min Client Profit: ", min(AllClientsGainTab))
        print("   Max Shop Profit: ", max(AllShopGainTab))
        print("   Min Shop Profit: ", min(AllShopGainTab), "\n")
    # print ( "\n")
