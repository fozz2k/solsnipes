# solsnipes

I am sure you have heard of dogwifhat, Mew, pepe climb, etc. 
There are many altcoins in the solana ecosystem that are mooning in this bullrun.
solsnipes is a solana altcoin sniper. 
Essentially, it finds new altcoins that our machine learning model predicts have potential to grow!

## Prerequisites
1. You must have python installed. Navigate to `https://www.python.org/downloads/` to download python.
2. Create a birdeye api key `@ https://bds.birdeye.so/`

## Configuration

1. Clone the github repo. This can be done by running `git clone https://github.com/calebjlee/solsnipes.git` in the folder you would like.
2. If you do not have requests installed run `pip install requests`
3. Navigate to `request.py` in the `./apps/components` folder.
4. Change the api key to the one you created in step 2 of Prerequisites.
5. Change `min` and `max` market cap values to your liking.
6. Adjust `offset`: `1920` is a good starting point to filter for coins below `300k` market cap.

## Running the Application

- Run `main.py` to create a `.log` file of all the coins in your market cap range:
  ```bash
  python main.py
  ```
- Rename folder and drag to the saved file.
- Run `filter.py` to filter the data:
  ```bash
  python filter.py
  ```

# Future Updates Coming

- We aim to filter coins to avoid rug pulls. Check out `strategy.txt` to see some of our ideas.
- We plan to use OpenAI to scan charts to identify healthy trading patterns using machine learning.
- We intend to connect a Solana wallet to UniSwap to automate our trades.
- We are looking to code an exit strategy for each coin sniped.
- We are planning on creating a website with the top altcoins listed to help other traders identify up and coming altcoins (NFA).
