const solanaWeb3 = require('@solana/web3.js');
const connection = new solanaWeb3.Connection(solanaWeb3.clusterApiUrl('mainnet-beta'), 'confirmed');

const SPL_TOKEN_PROGRAM_ID = new solanaWeb3.PublicKey("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA");

const getRecentTokenCreationTransactions = async () => {
    const signatures = await connection.getSignaturesForAddress(SPL_TOKEN_PROGRAM_ID);
    return signatures;
};

getRecentTokenCreationTransactions().then(async (signatures) => {
    // console.log(signatures);
    for (let i = 0; i < signatures.length; i++) {
        const transactionDetails = await connection.getTransaction(signatures[i], { commitment: 'confirmed' });
        console.log(transactionDetails);
    }
});
// Use this function to explore each transaction found in the previous step
