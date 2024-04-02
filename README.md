
# Solsnipes 🚀

Welcome to **Solsnipes** – your gateway to discovering potential moonshots within the Solana ecosystem! Sad that you missed out on trending tokens like **Dogwifhat**, **MEW**, and **Pepe Climb**? Our platform leverages machine learning to pinpoint emerging altcoins poised for growth! 🚀

## 📋 Prerequisites

Before you embark on your sniping journey, ensure you have the following:

- **Python**: Essential for running the scripts. Download the latest version at [Python Downloads](https://www.python.org/downloads/).
- **Birdeye API Key**: Generate yours at [Birdeye](https://bds.birdeye.so/).

## ⚙️ Configuration

Get started with these simple steps:

1. **Clone the Repo**: Clone `solsnipes` to your desired directory:
   ```bash
   git clone https://github.com/calebjlee/solsnipes.git
   ```
2. **Install Requests**: If not already installed:
   ```bash
   pip install requests
   ```
3. **Set Up**:
   - Navigate to `request.py` in the `./apps/components` folder.
   - Update the Birdeye API key with yours.
   - Adjust `min` and `max` market cap values as preferred.
   - Set `offset` (1920 is recommended for targeting coins below a 300k market cap).

## 🚀 Running the Application

Follow these steps to snipe your next potential moonshot:

- **Generate Log File**: Run `main.py` to compile a log of coins within your specified market cap range:
  ```bash
  python main.py
  ```
- **Organize**: Rename the folder as desired and move your `.log` file accordingly.
- **Filter Data**: Execute `filter.py` to sift through the data:
  ```bash
  python filter.py
  ```

# 🌟 Future Updates

Our roadmap is packed with exciting features aimed at enhancing your sniping strategy:

- **Rug Pull Defense**: Strategies to sidestep potential scams.
- **OpenAI Integration**: Employ machine learning for analyzing chart patterns.
- **Automated Trading**: Connect to UniSwap via a Solana wallet for seamless transactions.
- **Exit Strategy Coding**: Tailor-made strategies for each coin.
- **Community Website**: A hub for traders to discover and discuss promising altcoins. (NFA - Not Financial Advice)

Stay tuned for these updates and more as we continue to evolve Solsnipes for the community!
