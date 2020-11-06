# Date extraction using Regular Expressions: Knowledge Engineering Assignment
## 2020 November 6th

This is a simple python program to parse date expressions from input text with the use of regular expressions only.

## Usage
Just run:

`python main.py` 

You will be prompted to enter a text in a single line. On pressing `enter` the program lists all the parsed date expressions along with their positions in the string.


## Running tests
The file `test.py` contains possible test cases. Run:  

`python tests.py`


## Sample output
```
Enter the text in a single line: After an exhaustive 45-year investigation, the FBI in 2016 finally called off its official search for D.B. Cooper, the mysterious man who, on Nov. 24, 1971, hijacked a plane headed from Portland, Oregon to Seattle, Washington. In one of the most daring and unforgettable crimes in aviation history, he parachuted from the Boeing 727 with $200,000 in ransom money, eluding capture and enrapturing amateur sleuths worldwide.  In the decades that followed the brazen act, the bureau eliminated all but two of 1,000 suspects in the case. The most substantive leads included $5,800 of the ransom money found by a boy in 1980 along the Columbia River in Washington state, and taunting letters received by several U.S. newspapers. The letters, in particular, have offered tantalizing clues to the identity of the man behind the alias who got away with what would have been $1.2 million today.  READ MORE: Who Was D.B. Cooper?  DB Cooper Artist sketches of D.B. Cooper.  FBI At least six letters—typed, handwritten and made using ransom-style cut out letters—were sent to several newspapers soon after the hijacking, all claiming to be from Cooper. The FBI considered most to be hoaxes. But intriguingly, they held back the last two letters from the public until the 2000s, which may indicate they took those far more seriously.  A first letter, signed “DB Cooper” and sent from Oakdale, California to the Reno Evening Gazette, was received on November 29, 1971. Using letters cut and paste from a Sacramento Bee newspaper, it read: “Attention! Thanks for the hospitality. Was in a rut.” A second letter, handwritten and signed “D.B. Cooper,” was postmarked November 30, 1971 and sent to the Vancouver Province in British Columbia with the following message: 

------------ RESULTS ------------

Found 2016 at position 54
Found 1971 at position 151
Found 1980 at position 615
Found today at position 879
Found November 29, 1971 at position 1436
Found November 30, 1971 at position 1650
```
