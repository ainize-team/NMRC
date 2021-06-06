# NMRC
This is a crawler for movie review. This project includes

- A simple crawler (written in python)
- DB for firebase
- Simple functions (written in javascript) for preprocess and cron(not yet done)


## Okay! Time to run the crawler
Install pre-requisites, which are requests, bs4 and firebase_admin.

```
pip install requests bs4 firebase_admin
```

Run it

```
python crawler.py
```


## We also have got functions
### Pre-requisites
To use this, needs to, first of all, **set up firebase projects** as well as needs to generate
**firebase admin SDK** and download it. Then, download both the firebase admin SDK file(JSON) and a
firebase config file. Lastly, save the file into ./keys and ./functions/keys respectively. You are
up to start now!

### In detail
The functions is used for the preprocess pipeline, which is deployed on [Ainize API](https://ainize.ai/dleunji/korean_preprocessor_api?branch=master).
You are also able to use this on the [web](https://master-korean-preprocessor-dleunji.endpoint.ainize.ai/).

The function, preprocess, is called whenever raw data is inserted and the preprocessed text is
recorded triggered by this firebase functions.

cron(schedule) will be updated sooner.

See ./functions/

### Deploy functions
```
firebase deploy --only functions
```

## LICENSE

MIT License

Copyright (c) 2021 Ainize

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
