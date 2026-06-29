"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
  - SAMPLE_POSTS: short example posts for evaluation and training
  - TRUE_LABELS: human labels for each post in SAMPLE_POSTS
"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing",
    "proud",
    "hopeful",
    "surprised",
    "shook",
    "fire",
]

NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
    "annoying",
    "ghosted",
]

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Short example posts written as if they were social media updates or messages.
SAMPLE_POSTS = [
    "I love this class so much",
    "Today was a terrible day",
    "Feeling tired but kind of hopeful",
    "This is fine",
    "So excited for the weekend",
    "I am not happy about this",
    "Lowkey stressed but also proud of how far I came",
    "No cap, this week has been straight fire 😊",
    "I hate that I'm laughing at this sad meme 😂",
    "Honestly, feeling meh about everything rn",
    "Got ghosted again, so annoying 💀",
    "My friends surprised me and I'm shook",
    "Sometimes it's fine, sometimes it's not",
    "I absolutely love getting stuck in traffic",
    "This is actually pretty great :)",
    "I'm so tired of this nonsense",
    "Honestly, I'm feeling okay today",
    "This weekend was amazing and relaxing",
    "I really don't like being ignored",
    "The day started badly but ended well",
]

# Human labels for each post above.
# Allowed labels in the starter:
#   - "positive"
#   - "negative"
#   - "neutral"
#   - "mixed"
TRUE_LABELS = [
    "positive",  # "I love this class so much"
    "negative",  # "Today was a terrible day"
    "mixed",     # "Feeling tired but kind of hopeful"
    "neutral",   # "This is fine"
    "positive",  # "So excited for the weekend"
    "negative",  # "I am not happy about this"
    "mixed",     # "Lowkey stressed but also proud of how far I came"
    "positive",  # "No cap, this week has been straight fire 😊"
    "mixed",     # "I hate that I'm laughing at this sad meme 😂"
    "neutral",   # "Honestly, feeling meh about everything rn"
    "negative",  # "Got ghosted again, so annoying 💀"
    "positive",  # "My friends surprised me and I'm shook"
    "mixed",     # "Sometimes it's fine, sometimes it's not"
    "negative",  # "I absolutely love getting stuck in traffic"
    "positive",  # "This is actually pretty great :)"
    "negative",  # "I'm so tired of this nonsense"
    "neutral",   # "Honestly, I'm feeling okay today"
    "positive",  # "This weekend was amazing and relaxing"
    "negative",  # "I really don't like being ignored"
    "mixed",     # "The day started badly but ended well"
]

assert len(SAMPLE_POSTS) == len(TRUE_LABELS), (
    "SAMPLE_POSTS and TRUE_LABELS must have the same length"
)

# TODO: Add 5-10 more posts and labels.
#
# Requirements:
#   - For every new post you add to SAMPLE_POSTS, you must add one
#     matching label to TRUE_LABELS.
#   - SAMPLE_POSTS and TRUE_LABELS must always have the same length.
#   - Include a variety of language styles, such as:
#       * Slang ("lowkey", "highkey", "no cap")
#       * Emojis (":)", ":(", "🥲", "😂", "💀")
#       * Sarcasm ("I absolutely love getting stuck in traffic")
#       * Ambiguous or mixed feelings
#
# Tips:
#   - Try to create some examples that are hard to label even for you.
#   - Make a note of any examples that you and a friend might disagree on.
#     Those "edge cases" are interesting to inspect for both the rule based
#     and ML models.
#
# Example of how you might extend the lists:
#
# SAMPLE_POSTS.append("Lowkey stressed but kind of proud of myself")
# TRUE_LABELS.append("mixed")
#
# Remember to keep them aligned:
#   len(SAMPLE_POSTS) == len(TRUE_LABELS)
