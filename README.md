#Lyrics Grab

To install this, make sure you have Python installed, then open a terminal window inside the directory you have this folder downloaded in and run.

```
pip install -r requirements.txt
```

And then either

```
python artistgrab.py
```
or
```
python songgrab.py
```

# Register with Genius
In order to access the Genius API you need to register as a developer and get an access token.
Once you have this paste it into the token parameter in artistgrab and songgrab.

## Customising the output
Feel free to edit `artistlist.txt` and `songlist.txt` with whichever artists or songs you'd like.
To edit the number of songs grabbed per artist change the max_songs parameter inside `artistgrab.py`.

If you want to save a generated output file, make sure to rename it before running the software again or it will be overwritten
