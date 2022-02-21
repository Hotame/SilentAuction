from SilentAuctionArt import logo
from SAModerator import clearConsole

# Write Code 💻
print(logo)

bidder_Record = {}
end_Auction = False
    
while not end_Auction:
    name = input("\n\nKaede : What's Your Name -> ")
    bid = int(input("\n\nKaede : How Much Would You Like To Bid? -> $"))
    bidder_Record[name] = bid
        
    continue_Bidding = input("\n\nKaede : Are There Any Other Bidders? Y/N -> ").lower()

    if continue_Bidding == "n":
        end_Auction = True
        
    else:
        end_Auction = False
        clearConsole()
            
    highest_Bid = 0
    winner = ""
        
    for bidder in bidder_Record:
        if bidder_Record[bidder] > highest_Bid:
            highest_Bid = bidder_Record[bidder]
            winner = bidder
print(f"\n\nKaede : The Highest Bidder Is {winner}, With A Bid Of ${highest_Bid}\n")