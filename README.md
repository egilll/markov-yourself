# Markov yourself, using your Facebook messages

This is a script to:

1. Convert all of your Facebook messages into JSON format
2. Extract all messages from a specific person
3. Create a Markov chain that'll speak like that person


---


### Step 1: Download all your Facebook data

Download your Facebook data & messages by going to 
    Settings → General Account Settings → 
    Download a copy of your Facebook data → Start My Archive.


### Step 2: Parse your messages

Move the `messages.htm` file into the same folder as these scripts.

Import the needed Python packages:

```
pip install beautifulsoup4
pip install markovify
```


**In `messages.py`, change the `name` at top to your desired name**.

Now run (this will take a while):

`> python messages.py`

Two files will be created:

1. `facebook_messages.json` containing all your messages in
    JSON format (will not be used for the Markov thing, 
    but it's there if you want to do something with it)
2. `messages_from_this_name.txt` which we'll use for the Markov chain


### Step 3: Output Markov

Running:

`> python markov.py`

will generate several sentences.

The sentence sections are:

1. Long sentences, markovified by periods. 
   This will produce more hilarious output,
   but is not a 'correctly' trained Markov chain
   since in the file we had created earlier,
   messages_from_this_name.txt,
   messages are split by newline, 
   and periods are rare in chats.
2. Short sentences markovified by periods.
3. Long sentences, markovified by newline. This will produce
   shorter & dryer sentences than in section 1,
   but they'll be more correct.
4. Short sentences markovified by newline. 
