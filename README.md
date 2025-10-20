## 📰 Text Summarization
This project is a **Natural Language Processing (NLP)** application that automatically generates concise summaries from long news articles using the T5 transformer model.<br>
It leverages abstractive summarization, meaning the model learns to rephrase the text in its own words rather than simply extracting sentences.

## 🧩 Key Steps:
- **Data Cleaning (slight cleaning):** Removed HTML tags, URLs, and extra spaces; tokenized and normalized text using NLTK and BeautifulSoup.
- **Model:** Fine-tuned the **T5 model** for summarization.
- **Preprocessing:** Long text inputs were truncated to fit the model’s input limit.
- **Evaluation:** Computed ROUGE-1, ROUGE-2, and ROUGE-L scores to assess summary quality.
- **Comparison:** Evaluated abstractive vs. extractive summarization methods (TextRank).
- **Deployment:** Built an interactive Streamlit app for users to input any article and get instant summaries.

## 📂 Dataset
The dataset used is the CNN-DailyMail News Dataset (300,000+ samples).
- Available on:
  - [Kaggle - CNN-DailyMail News Dataset](https://www.kaggle.com/datasets/gowrishankarp/newspaper-text-summarization-cnn-dailymail)

## 📊 Model Evaluation
| Epoch | Training Loss | Validation Loss | ROUGE-1 | ROUGE-2 | ROUGE-L |
| :---- | :------------ | :-------------- | :------ | :------ | :------ |
| **1** | 1.2652        | 1.2219          | 0.2434  | 0.1136  | 0.1996  |
| **2** | 1.2128        | 1.2057          | 0.2462  | 0.1154  | 0.2015  |
| **3** | 1.1971        | 1.2019          | 0.2467  | 0.1159  | 0.2022  |

## 🧠 Tech Stack & Tools: 
- **Python Libraries**:  
  `Pandas`, `NLTK`, `spacy`, `BeautifulSoup`, `pytextrank`, `Datasets`, `rouge-score`, `Transformers`
- **Deployment**: Streamlit for interactive prediction  
- **Others**: GitHub / Google Colab / Kaggle for experimentation

## 📦 Dependencies
Before running this project locally, ensure the following are installed:
```sh
pip install pandas datasets nltk spacy beautifulsoup4 pytextrank rouge-score transformers streamlit
```

## Installing
To install Streamlit:
```sh
pip install streamlit
```
To install all required dependencies:
```sh
pip install -r requirements.txt
```

## Running the Application Locally
```sh
streamlit run app.py
```
Then open the local URL (usually http://localhost:8501/) in your browser.

## Try the App Online
You can use the app directly here: [Review Predictor](https://concise-summary.streamlit.app/)<br>
Simply paste any long text or news article and click **Summarize** to generate an abstract summary.

## 💡 Features
- Clean and preprocess raw text
- Perform abstractive and extractive summarization
- Fine-tune T5-Small for abstractive summarization
- Evaluate summary quality using ROUGE metrics
- Deploy an interactive web app via Streamlit
  
## 📂 Folder Structure
```
Text-Summarization-PreTrained-Models/
├── app.py
├── requirements.txt
└── README.md
    
```

## ❓ Help
If you encounter any issues:
- Check the [Streamlit Documentation](https://docs.streamlit.io/)
- Search for similar issues or solutions on [Kaggle](https://www.kaggle.com/)
- Open an issue in this repository

## ✍️ Author
👤 Oluyale Ezekiel
- 📧 Email: ezekieloluyale@gmail.com
- LinkedIn: [Ezekiel Oluyale](https://www.linkedin.com/in/ezekiel-oluyale)
- GitHub Profile: [@amusEcode1](https://github.com/amusEcode1)
- Twitter: [@amusEcode1](https://x.com/amusEcode1?t=uHxhLzrA1TShRiSMrYZQiQ&s=09)

## 🙏 Acknowledgement
Thank you, Elevvo, for the incredible opportunity and amazing Internship.
