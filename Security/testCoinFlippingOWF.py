from ahc.Ahc import *
from ahc.Channels.Channels import Channel
from ahc.Security.CoinFlippingOWF import *
import networkx
import random
import hashlib
from time import  sleep

def main():
    print("\n\n**********************************************")
    print("****                                          ****")
    print("****   Welcome To Explanation of              ****")
    print("****       Fair Coin Flipping                 ****")
    print("****         using One-Way function (sha256)  ****")
    print("****                                          ****")
    print("**************************************************\n\n")
    setup_topology()
    sleep(15)

if __name__ == "__main__":
    main()       