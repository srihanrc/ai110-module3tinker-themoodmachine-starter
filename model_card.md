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

The dataset had sentences that were difficult to determine whether the mood was mixed or neutral. At first the ML model never predicted the mood as mixed because it hadn't learned those patterns yet till after adding mixed mood into ML training.

## 3. How the Rule Based Model Works (if used)

**Your scoring rules:**  
Describe the modeling choices you made.  
Examples:  

- How positive and negative words affect score  
- Negation rules you added  
- Weighted words  
- Emoji handling  
- Threshold decisions for labels

Positive words were +1 to score and negative words were -1 to score. For negation I made a list of negation words and then if the negation word is in the sentence it would look at the next word and best on the mood for that word the model would label the opposite choice.

**Strengths of this approach:**  
Where does it behave predictably or reasonably well?

It's able to understand positive and negative words.

**Weaknesses of this approach:**  
Where does it fail?  
Examples: sarcasm, subtlety, mixed moods, unfamiliar slang.

It fails when there's a negation, this misses the negation word and therefore gives the wrong label.

## 4. How the ML Model Works (if used)

**Features used:**  
Describe the representation.  
Example: “Bag of words using CountVectorizer.”

The mood machine uses the list and splits the sentence into tokens. After the text is preprocessed, the program checks each word with the set of positive and negative words. If the word is positive the mood score increases by 1 and if negative the mood score decreases by 1.

**Training data:**  
State that the model trained on `SAMPLE_POSTS` and `TRUE_LABELS`.

`SAMPLE_POSTS` was used as input text sentence examples while `TRUE_LABELS` was used as correct mood labels. 

**Training behavior:**  
Did you observe changes in accuracy when you added more examples or changed labels?

Yes I noticed the accuracy was really low when I added more labels that were mixed. 

**Strengths and weaknesses:**  
Strengths might include learning patterns automatically.  
Weaknesses might include overfitting to the training data or picking up spurious cues.

One strength from the model is that this can learn patterns from training data instead of just lists of positive and negative words. This training data helps the model predict the mood labels.

## 5. Evaluation

**How you evaluated the model:**  
Both versions can be evaluated on the labeled posts in `dataset.py`.  
Describe what accuracy you observed.

I evaluated the model through accuracy which is total true_labels divided by the correct predictions to get the percentage accuracy of the model.

**Examples of correct predictions:**  
Provide 2 or 3 examples and explain why they were correct.

"positive",  # "This is actually pretty great :)". This is correct because this sentence uses a smily face and uses the keyword great.

"negative",  # "I'm so tired of this nonsense". This is correct because this uses the keyword tired and nonsense indicating the users frustration.

"neutral",   # "Honestly, I'm feeling okay today". This is correct because this is uses the keyword okay indicating that the user is in between of feeling great and bad.

**Examples of incorrect predictions:**  
Provide 2 or 3 examples and explain why the model made a mistake.  
If you used both models, show how their failures differed.

"mixed",     # "Sometimes it's fine, sometimes it's not". The model made this mistake because it didn't mixed was a label as this wasn't apart of the model training and therefore the model predicted neutral instead.

"negative",  # "I absolutely love getting stuck in traffic". The model made this mistake because it didn't understand negations and therefore heavily relied on the keyword to make it's prediction.

## 6. Limitations

Describe the most important limitations.  
Examples:  

- The dataset is small  
- The model does not generalize to longer posts  
- It cannot detect sarcasm reliably  
- It depends heavily on the words you chose or labeled

I think the dataset is a bit small but it definitely uses a lot of test case scenarios to where I am confident that the model is performing really well. I think one limitation would be that the model probably can't fully detect negation words just yet.

## 7. Ethical Considerations

Discuss any potential impacts of using mood detection in real applications.  
Examples: 

- Misclassifying a message expressing distress  
- Misinterpreting mood for certain language communities  
- Privacy considerations if analyzing personal messages

Using mood detection may cause misclassification in how the person actually feels. For example someone whose really upset may use a lot of sarcasm in their sentences and the model may fail to detect the sarcasm in each sentence. This would be really impactful in work environments as coworkers would get the wrong idea of how you feel. 

## 8. Ideas for Improvement

List ways to improve either model.  
Possible directions:  

- Add more labeled data  
- Use TF IDF instead of CountVectorizer  
- Add better preprocessing for emojis or slang  
- Use a small neural network or transformer model  
- Improve the rule based scoring method  
- Add a real test set instead of training accuracy only

For the models I would add more labeled training data so that this would learn from more different types of posts. That way the model would perform better on the new data instead of just a small example. I also think using a better model like neural networks would work as well since this would be able to understand the meaning of text for the sentences.  
