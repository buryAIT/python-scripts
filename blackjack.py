import math;
import random;
import os
from time import sleep;
import ftfy;


class Deck:
    
    def __init__(self, deckCount):
        
        self.deckCount = deckCount
    
    cardCount = 0;
    
    #Hearts
    Ace_H = "\U0001F0B1"
    Two_H = "\U0001F0B2"
    Three_H = "\U0001F0B3"
    Four_H = "\U0001F0B4"   
    Five_H = "\U0001F0B5"
    Six_H = "\U0001F0B6"
    Seven_H = "\U0001F0B7"
    Eight_H = "\U0001F0B8"
    Nine_H = "\U0001F0B9"
    Ten_H = "\U0001F0BA"
    Jack_H = "\U0001F0BB"
    Queen_H = "\U0001F0BD"
    King_H = "\U0001F0BE"
    
    #Diamonds
    Ace_D = "\U0001F0C1"
    Two_D = "\U0001F0C2"
    Three_D = "\U0001F0C3"
    Four_D = "\U0001F0C4"
    Five_D = "\U0001F0C5"
    Six_D = "\U0001F0C6"
    Seven_D = "\U0001F0C7"
    Eight_D = "\U0001F0C8"
    Nine_D = "\U0001F0C9"
    Ten_D = "\U0001F0CA"
    Jack_D = "\U0001F0CB"
    Queen_D = "\U0001F0CD"
    King_D = "\U0001F0CE"
    
    #Clubs
    Ace_C = "\U0001F0D1"
    Two_C = "\U0001F0D2"
    Three_C = "\U0001F0D3"
    Four_C = "\U0001F0D4"
    Five_C = "\U0001F0D5"
    Six_C = "\U0001F0D6"
    Seven_C = "\U0001F0D7"
    Eight_C = "\U0001F0D8"
    Nine_C = "\U0001F0D9"
    Ten_C = "\U0001F0DA"
    Jack_C = "\U0001F0DB"
    Queen_C = "\U0001F0DD"
    King_C = "\U0001F0DE"
    
    #Spades
    Ace_S = "\U0001F0A1"
    Two_S = "\U0001F0A2"
    Three_S = "\U0001F0A3"
    Four_S = "\U0001F0A4"
    Five_S = "\U0001F0A5"
    Six_S = "\U0001F0A6"
    Seven_S = "\U0001F0A7"
    Eight_S = "\U0001F0A8"
    Nine_S = "\U0001F0A9"
    Ten_S = "\U0001F0AA"
    Jack_S = "\U0001F0AB"
    Queen_S = "\U0001F0AD"
    King_S = "\U0001F0AE"
   
    
    normalDeck = [ 
    #Hearts     #Diamonds   #Clubs      #Spades
    Ace_H,      Ace_D,      Ace_C,      Ace_S,
    Two_H,      Two_D,      Two_C,      Two_S,
    Three_H,    Three_D,    Three_C,    Three_S,
    Four_H,     Four_D,     Four_C,     Four_S,
    Five_H,     Five_D,     Five_C,     Five_S,
    Six_H,      Six_D,      Six_C,      Six_S,
    Seven_H,    Seven_D,    Seven_C,    Seven_S,
    Eight_H,    Eight_D,    Eight_C,    Eight_S,
    Nine_H,     Nine_D,     Nine_C,     Nine_S,
    Ten_H,      Ten_D,      Ten_C,      Ten_S,
    Jack_H,     Jack_D,     Jack_C,     Jack_S,
    Queen_H,    Queen_D,    Queen_C,    Queen_S, 
    King_H,     King_D,     King_C,     King_S,
                       
                       ]
    
    
    deckOfRemaining = normalDeck.copy();

    
    DictionaryDeck = {
        
    #Hearts                         #Diamonds                       #Clubs                          #Spades
    Ace_H : ["Ace_H", 1, 11],       Ace_D : ["Ace_D", 1, 11],       Ace_C : ["Ace_C", 1, 11],       Ace_S : ["Ace_S", 1, 11],
    Two_H : ["Two_H", 2],           Two_D : ["Two_D", 2],           Two_C : ["Two_C", 2],           Two_S : ["Two_S", 2],
    Three_H : ["Three_H", 3],       Three_D : ["Three_D", 3],       Three_C : ["Three_C", 3],       Three_S : ["Three_S", 3],
    Four_H : ["Four_H", 4],         Four_D : ["Four_D", 4],         Four_C : ["Four_C", 4],         Four_S : ["Four_S", 4],
    Five_H : ["Five_H", 5],         Five_D : ["Five_D", 5],         Five_C : ["Five_C", 5],         Five_S : ["Five_S", 5],
    Six_H : ["Six_H", 6],           Six_D : ["Six_D", 6],           Six_C : ["Six_C", 6],           Six_S : ["Six_S", 6],
    Seven_H : ["Seven_H", 7],       Seven_D : ["Seven_D", 7],       Seven_C : ["Seven_C", 7],       Seven_S : ["Seven_S", 7],
    Eight_H : ["Eight_H", 8],       Eight_D : ["Eight_D", 8],       Eight_C : ["Eight_C", 8],       Eight_S : ["Eight_S", 8],
    Nine_H : ["Nine_H", 9],         Nine_D : ["Nine_D", 9],         Nine_C : ["Nine_C", 9],         Nine_S : ["Nine_S", 9],
    Ten_H : ["Ten_H", 10],          Ten_D : ["Ten_D", 10],          Ten_C : ["Ten_C", 10],          Ten_S : ["Ten_S", 10],
    Jack_H : ["Jack_H", 10],        Jack_D : ["Jack_D", 10],        Jack_C : ["Jack_C", 10],        Jack_S : ["Jack_S", 10],
    Queen_H : ["Queen_H", 10],      Queen_D : ["Queen_D", 10],      Queen_C : ["Queen_C", 10],      Queen_S : ["Queen_S", 10], 
    King_H : ["King_H", 10],        King_D : ["King_D", 10],        King_C : ["King_C", 10],        King_S : ["King_S", 10],
        
    }
    
    
    def evaluateHandTotal( self, hand ):
        
        aceLowTotal = 0;
        aceHighTotal = 0;
        
        total = 0;
        for card in hand:
            
             
            if ( str( self.DictionaryDeck[ card ][ 0 ] ).startswith("A") == False ):
                aceLowTotal += self.DictionaryDeck[ card ][ 1 ];
                aceHighTotal += self.DictionaryDeck[ card ][ 1 ];

            else:
                
                aceLowTotal += self.DictionaryDeck[ card ][ 1 ];
                aceHighTotal += self.DictionaryDeck[ card ][ 2 ]
            
        if ( aceHighTotal > 21 ):
            total = aceLowTotal;
        else:
            total = aceHighTotal;
            
        return total;
    
    
    def handWon(self, playerTotal, dealerTotal ):
        
        if( playerTotal == dealerTotal ):
            return "push";
        elif( playerTotal == 21 ):
            return True;
        elif( dealerTotal == 21 ):
            return False;
        elif( playerTotal > dealerTotal and playerTotal < 21 ):
            return True;
        elif( dealerTotal > 21 ):
            return True;
        else:
            return False;
    
    
    
    def shuffle(self):
        self.normalDeck = self.deckOfRemaining.copy();
    
    
    def drawCard(self, count ):
        cardlist = [ ]; 
        
        
        
        for i in range( count ):
            
            
            if ( len ( self.normalDeck ) == 0 ):
                self.shuffle()
        
            cardIndex = random.randint( 0, len( self.normalDeck ) - 1 );
            card = self.normalDeck.pop( cardIndex );
            cardlist.append( card );
            self.cardCount = len ( self.normalDeck );
        
        return cardlist;



class Player:
    def __init__(self):
        pass
    
    running = False;
    dealer = [];
    hand = [];
    sideHand1 = [];
    sideHand2 = [];
    AccountValue = 0;
    bet = 0;
    currentlyInEndgame = False;
    
    def addValue( self, amount ):
        self.AccountValue += amount;
    
    def minusValue( self, amount ):
        self.AccountValue -= amount;
    
    def betValue( self, amount ):
        
        if( amount <= self.AccountValue ):
            self.bet += amount;
        else:
            print(" Not Enough Money, Please try again ");
            sleep(3);
            self.initialBet();
            
    def initialBet( self ):
        
        os.system("clear");
        print( "You have $" + str(self.AccountValue) + ", What is your bet?" );

        while True:
            try:
                currentBet = input( "--> " );
                if( currentBet == "" ):
                    currentBet = self.bet;
                currentBet = int( currentBet );
                break;
            except ValueError:
                print( "Please enter a number" );
                
        print( "Press enter if " + "$" + str(currentBet) + " is correct " );
        verify = input( "-->" );
        
        if( currentBet > 0 and verify == "" ):
            self.betValue( currentBet );
        else:
            for i in range(3):
                a = 3 - i;
                os.system("clear")
                print("Re-enter bet in " + str(a) );
                sleep(1);
                
            self.initialBet();
            
            
            
    def endGame( self, handWon, playerTotal, dealerTotal):
        
        
        if ( handWon == "Blackjack" ):
            print( "You hit a Blackjack!! Congrats!!" );
            blackjack = self.bet * 3 / 2;
            self.addValue( blackjack );
            self.bet = 0;
        
        elif ( handWon == "push" ):
            print( "You and the dealer had a matching total of " + str( playerTotal ) );
            self.bet = 0;
            
        elif( handWon ):
            print( "You won this hand with a total of " + str( playerTotal ) + ", while the dealer had a total of " + str( dealerTotal ));
            self.addValue( self.bet );
            self.bet = 0;
        else:
            print( "You lost this hand with a total of " + str( playerTotal ) + ", while the dealer had a total of " + str( dealerTotal ));
            self.minusValue( self.bet );
            self.bet = 0;
            
        #implements the continue button
        print( " - - - - > Current Account Total: $" + str(self.AccountValue) + " < - - - - " )
        print( " - - - - - > Press Enter To Continue : < - - - - - " );
        
        forward = input();
        
        
        if( self.AccountValue == 0 ):
            os.system("clear");
            print("You have run out of money!")
            print("Please deposit more to continue");
            print("")
            print("Press Enter to exit");
            input();
            self.running = False;
        
        
        if ( forward == "" ):
            os.system( "clear" );
        else:
            self.running = False;
    
    
    
            
    
    
    

def run():
    
    deck = Deck(1);

    player = Player();

    player.addValue(100);

    
    
    while( player.running == True ):

        player.currentlyInEndgame = False;
        
        player.initialBet();

        handWon = False;
        player.hand = deck.drawCard( 2 );
        player.dealer = deck.drawCard( 2 );
        pCard1 = player.hand[0];
        pCard2 = player.hand[1];
        dCard1 = player.dealer[0];
        dCard2 = player.dealer[1];
        
        if( deck.evaluateHandTotal( player.hand ) == 21 ):
            print(" !!BLACKJACK!!");
            print( "Your hand: " + str(player.hand) );
            print( "Dealers hand: " + str(player.dealer) );
            player.endGame( "Blackjack", 21, 0);
            continue;
        
        elif( deck.evaluateHandTotal( player.dealer ) == 21 ):
            print("Unfortunate");
            print( "Your hand: " + str(player.hand) );
            print( "Dealers hand: " + str(player.dealer) );
            player.endGame( False, deck.evaluateHandTotal( player.hand ), 21);
            continue;
        
        print( str(pCard1) + " and " + str(pCard2) + " are your cards, the dealer has a " + str(dCard1) + " face up.") ;
        playerTotal = deck.evaluateHandTotal(player.hand);
        dealerTotal = deck.evaluateHandTotal(player.dealer);
        print( str( pCard1 ) + " and " + str( pCard2 ) + " equals " + str(playerTotal) + ", what do you want to do? " );
        print("Hit, Stand, Double, or Split?")
        action = input()
        
        for i in range(10):
        
            if( action.upper() == "HIT" ):
                
                player.hand.append( deck.drawCard(1).pop() );
                
                if( deck.evaluateHandTotal( player.hand ) <= 21 ):
                    print( "Your hand is now " + str(player.hand) );
                    print("Hit, Stand, Double, or Split?");
                    action = input();
                else:
                                
                    print( "Your hand: " + str(player.hand) );
                    print( "Dealers hand: " + str(player.dealer) );
                    player.currentlyInEndgame = True;
                    player.endGame(  False, deck.evaluateHandTotal( player.hand ), deck.evaluateHandTotal( player.dealer ) )
                    break;
            
            elif( action.upper() == "DOUBLE"):
                
                if( player.bet <= player.AccountValue / 2 ):
                    player.bet *= 2;
                    player.hand.append( deck.drawCard(1).pop() );
                    break;
                
                else:
                    print("Invalid Option, proceeding to Stand");
                    sleep(3);
                    break;
            
            elif( action.upper() == "SPLIT" ):
                
                if ( deck.DictionaryDeck[pCard1][1] == deck.DictionaryDeck[pCard2][1] and player.bet <= player.AccountValue / 2 ):
                    
                    sideBet1 = player.bet;
                    sideBet2 = player.bet;
                    player.bet = 0;
                    player.sideHand1 = [pCard1, deck.drawCard(1).pop() ];
                    player.sideHand2 = [pCard2, deck.drawCard(1).pop() ];
                    print( "Here's your first hand: " + str(player.sideHand1) );
                    print( "What do you want to do? " );
                    print( "Hit, Stand, or Double? " );
                    
                    sideAction = input();
                    
                    for i in range( 10 ):
                        if( sideAction.upper() == "HIT" ):
                    
                            player.sideHand1.append( deck.drawCard(1).pop() );
                            
                            if( deck.evaluateHandTotal( player.sideHand1 ) <= 21 ):
                                print( "Your hand is now " + str( player.sideHand1 ) );
                                print("Hit or Stand ?");
                                sideAction = input();
                            else:
                                            
                                print( "Your hand: " + str( player.sideHand1 ) );
                                break;
                        
                        elif( sideAction.upper() == "DOUBLE"):
                            
                            if( sideBet1 <= player.AccountValue / 4 ):
                                sideBet1 *= 2;
                                player.sideHand1.append( deck.drawCard(1).pop() );
                                break;
                            
                            else:
                                print("Invalid Option, proceeding to Stand");
                                sleep(3);
                                break;
                            
                        else:
                            break;
                    
                    os.system("clear");
                    
                    sideHandTotal = deck.evaluateHandTotal( player.sideHand1 );
                    
                    if( deck.handWon( sideHandTotal, deck.evaluateHandTotal(player.dealer) ) == True ):
                        print( "You won this hand with " + str(player.sideHand1) );
                        player.AccountValue += sideBet1;
                    else:
                        print( "You lost this hand with " + str(player.sideHand1) );
                        player.AccountValue -= sideBet1;
                    
                    print("")
                        
                    
                    print(" - - - - - - - - - - ");
                        
                    print( "Here's your second hand: " + str(player.sideHand2) );
                    print( "What do you want to do? " )
                    print( "Hit, Stand, or Double? " )
                    sideAction = input();
                    
                    
                    for i in range( 10 ):
                        if( sideAction.upper() == "HIT" ):
                    
                            player.sideHand2.append( deck.drawCard(1).pop() );
                            
                            if( deck.evaluateHandTotal( player.sideHand2 ) <= 21 ):
                                print( "Your hand is now " + str( player.sideHand2 ) );
                                print("Hit or Stand ?");
                                sideAction = input();
                            else:
                                            
                                print( "Your hand: " + str( player.sideHand2 ) );
                                break;
                        
                        elif( sideAction.upper() == "DOUBLE"):
                            
                            if( sideBet2 <= player.AccountValue / 4 ):
                                sideBet2 *= 2;
                                player.sideHand2.append( deck.drawCard(1).pop() );
                                break;
                            
                            else:
                                print("Invalid Option, proceeding to Stand");
                                sleep(3);
                                break;
                            
                        else:
                            break;
                    
                    os.system("clear");
                    
                    if( deck.handWon( deck.evaluateHandTotal( player.sideHand2 ), deck.evaluateHandTotal(player.dealer) ) == True ):
                        print( "You won this hand with " + str(player.sideHand2) );
                        player.AccountValue += sideBet2;
                        break;
                    else:
                        print( "You lost this hand with " + str(player.sideHand2) );
                        player.AccountValue -= sideBet2;
                        break;
                else:
                    print("Invalid Option, proceeding to Stand");
                    sleep(3);
                    break;

            else:
                break;
            
        if( player.currentlyInEndgame ):
            continue;
        
        for i in range(10):
            if( dealerTotal < 17 ):
                player.dealer.append( deck.drawCard(1).pop() );
                dealerTotal = deck.evaluateHandTotal( player.dealer );
            else:
                break;
            
        
        
        playerTotal = deck.evaluateHandTotal(player.hand);
        dealerTotal = deck.evaluateHandTotal(player.dealer);
        
        #adds messages for wins or losses
        
        handWon = deck.handWon( playerTotal, dealerTotal)
        
        print( "Your hand: " + str(player.hand) );
        print( "Dealers hand: " + str(player.dealer) );
        
        player.endGame( handWon, playerTotal, dealerTotal );



def startGame():
    
    os.system("clear");
    print( 
"\
!!Welcome to Blackjack!!\n\
^----------------------^\n\
^----------------------^\n\
^----------------------^\n\
^----------------------^\n\
^----------------------^\n\
^----------------------^\n"  
        )
    
    
    
    
    
    print("    Press Enter key      ")
    input()
    os.system('clear')
    
    Player.running = True;
    run();
    
    

    

startGame();