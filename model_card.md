# Model Card: Mood Machine

This model card is for the Mood Machine project, which includes **two** versions of a mood classifier:

1. A **rule based model** implemented in `mood_analyzer.py`
2. A **machine learning model** implemented in `ml_experiments.py` using scikit learn

You may complete this model card for whichever version you used, or compare both if you explored them.

## 1. Model Overview

**Model type:**  
Describe whether you used the rule based model, the ML model, or both.  
Example: “I used the rule based model only” or “I compared both models.”

I used both the models. I used the rule based model in the beginning and then used the ML model to compare the predictions with these models. 

**Intended purpose:**  
What is this model trying to do?  
Example: classify short text messages as moods like positive, negative, neutral, or mixed.

The model is trying to read text and look for key words like happy, sad, etc to identify the mood for each sentence.

**How it works (brief):**  
For the rule based version, describe the scoring rules you created.  
For the ML version, describe how training works at a high level (no math needed).

For the rule based version, if the word is in positive_words, the score is +1. Otherwise if it's in negative_words the score is -1. If the word is neutral or mixed, the score remains at 0. For the ML version it takes sample sentences from dataset.py and then converts the sentences into single word representations. This then pairs each sentence with the correct label given in TRUE_LABELS. The model learns these patterns during training such as which words are associated with positive, negative, neutral and mixed moods leading to increase of accuracy in predicting the right label.



## 2. Data

**Dataset description:**  
Summarize how many posts are in `SAMPLE_POSTS` and how you added new ones.

There are 20 sample posts and I added new ones by asking the AI assistant to make new posts based on the different edge cases to see if the model really did do well.

**Labeling process:**  
Explain how you chose labels for your new examples.  
Mention any posts that were hard to label or could have multiple valid labels.

I chose labels based on the key words in the sentences like happy would be a positive label. The posts that had words like not happy and sarcasm like "I absolutely love getting stuck in traffic" were definitely hard for the model to figure out.

**Important characteristics of your dataset:**  
Examples you might include:  

- Contains slang or emojis  
- Includes sarcasm  
- Some posts express mixed feelings  
- Contains short or ambiguous messages

Dataset had sarcasm sentences and sentences that had mixed emotions. Some sentences were straightforward and easy to understand.

**Possible issues with the dataset:**  
Think about imbalance, ambiguity, or missing kinds of language.



## 3. How the Rule Based Model Works (if used)

**Your scoring rules:**  
Describe the modeling choices you made.  
Examples:  

- How positive and negative words affect score  
- Negation rules you added  
- Weighted words  
- Emoji handling  
- Threshold decisions for labels

**Strengths of this approach:**  
Where does it behave predictably or reasonably well?

**Weaknesses of this approach:**  
Where does it fail?  
Examples: sarcasm, subtlety, mixed moods, unfamiliar slang.

## 4. How the ML Model Works (if used)

**Features used:**  
Describe the representation.  
Example: “Bag of words using CountVectorizer.”

**Training data:**  
State that the model trained on `SAMPLE_POSTS` and `TRUE_LABELS`.

**Training behavior:**  
Did you observe changes in accuracy when you added more examples or changed labels?

**Strengths and weaknesses:**  
Strengths might include learning patterns automatically.  
Weaknesses might include overfitting to the training data or picking up spurious cues.

## 5. Evaluation

**How you evaluated the model:**  
Both versions can be evaluated on the labeled posts in `dataset.py`.  
Describe what accuracy you observed.

**Examples of correct predictions:**  
Provide 2 or 3 examples and explain why they were correct.

**Examples of incorrect predictions:**  
Provide 2 or 3 examples and explain why the model made a mistake.  
If you used both models, show how their failures differed.

## 6. Limitations

Describe the most important limitations.  
Examples:  

- The dataset is small  
- The model does not generalize to longer posts  
- It cannot detect sarcasm reliably  
- It depends heavily on the words you chose or labeled

## 7. Ethical Considerations

Discuss any potential impacts of using mood detection in real applications.  
Examples: 

- Misclassifying a message expressing distress  
- Misinterpreting mood for certain language communities  
- Privacy considerations if analyzing personal messages

## 8. Ideas for Improvement

List ways to improve either model.  
Possible directions:  

- Add more labeled data  
- Use TF IDF instead of CountVectorizer  
- Add better preprocessing for emojis or slang  
- Use a small neural network or transformer model  
- Improve the rule based scoring method  
- Add a real test set instead of training accuracy only
