
# Resume Scanning 

The goal is to cluster resumes into relevant categories using the CorEx topic model and analyze the most common words and topics. This can help with tasks like automatically scanning and classifying resumes for job applications, making the process faster and more efficient.

## Technologies Used
- **Python**: The core language used for development
- **Pandas**, **Numpy**: for data manipulation and analysis
- **Scikit-learn**: for preprocessing
- **CorexTopic**: for CorEx topic modeling
- **Matplotlib**: for visualizations
- **NLP Techniques**: Count Vectorizer, text cleaning, tokenization
- **Flask**: For deployment as a web application.

## Project Workflow
1. **Data Preparation**: Load and preprocess the resume dataset.
2. **Text Processing**: Apply cleaning, stopword removal, and tokenization.
3. **Topic Modeling**: Use the CorEx model to assign topics to resumes.
4. **Analysis**: Visualize the distribution of topics and explore which resumes fall under specific categories.

## How to Run the Project
1. Clone this repository: `git clone https://github.com/pelinoz/Ozgecmis-Tarama-Sistemi.git`
2. Run the core script: `python app.py`
3. View the results of the topic modeling in the output folder or visualize the topics using matplotlib plots.

