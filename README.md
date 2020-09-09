# dispy





## how to use

1. install requrements.
1. rename `config.py.sample` file to `config.py` and fill it with your own information.
1. add your favorite static messages like welcome message and help message.
1. enjoy.


## static data (static messages)

There is some messages that we have to send them many times to many people like help message, welcome message, channel rules and many others.

static messages folder will contain this messages

#### accessing the static messages

send a message in this pattern to bot. a dollar sign then name of the static message.

>$name

some examples here :
```PHP
$help
$welcome
$author
```

## static data formatting

First 5 lines of each static message will be used for formatting that message.
If there is only 5 lines or even fewer than 5 lines, formatting will be ignored.

Each line should have just one command.
Enter command name then ':' and then its parameter (don't use spaces around ':' and in start and end of a command).


Commands :
1. **__hidden__**
  * description= users will not be able to access this static message directly ($name).
  * usage= `hidden`
  * example= `hidden`
2. **__image__**
  * description= set image of the message. if you pass a link image will be an embed but if pass path to an image, it will be a file (i mean 'discord.Embed' & 'discord.File').
  * usage=  `image:\<path to a local image file or a link to an image in internet\>`
  * example= `image:images\icon.png`
3. **__next__**
  * description= immediately send another static message after this once.
  * usage= `next:\<name of an static message\>`
  * example= `next:author`


## requirements

1. [discord.py](https://pypi.org/project/discord.py/)
* **installing**:
  * >python -m pip install -U discord.py

* [**documentation**](https://discordpy.readthedocs.io/en/latest/)
