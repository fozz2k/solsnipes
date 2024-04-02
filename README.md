# solsnipes

solsnipes is a solana altcoin sniper. 
Essentially, it finds new altcoins that our machine learning model predicts have potential to grow

## Configuration

1. Navigate to `request.py` in the `./apps/components` folder.
2. Change `min` and `max` market cap values to your liking.
3. Adjust `offset`: `1920` is a good starting point to filter for coins below `300k` market cap.

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
