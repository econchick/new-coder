## How to Contribute

[newcoder.io](http://newcoder.io) is a beloved pet project of mine.  But I have a full time job as well as running [PyLadiesSF](http://www.meetup.com/pyladiessf) and popping up at different [conferences](http://www.roguelynn.com/talks).  So, I’d love your help!

If you have a particular issue, navigate to either [Website issues](#website-issues) or [Tutorial code issues](#tutorial-code-issues).  If you want to just help, there are plenty of [reported issues](https://github.com/econchick/new-coder/issues?state=open) that could be knocked out, or checkout the [todos](#todos) below.


0. [New Coder project layout](#layout)
1. [Setup](#setup)
1. [Website issues](#website-issues)
2. [Tutorial code issues](#tutorial-code-issues)
3. [Suggestions](#suggestions)
4. [Helping our new coders](#helping-our-new-coders)
5. [ToDos](#todos)



### Layout

The New Coder repository has the following layout:

```bash
.
├── apis/
│   ├── README.md
│   └── # code
├── dataviz/
│   ├── README.md
│   └── # code
├── gui/
│   ├── README.md
│   └── # code
├── network/
│   ├── README.md
│   └── # code
├── scrape/
│   ├── README.md
│   └── # code
└── website/
    ├── _assets/  # all css, images, etc
    ├── _posts/  # all posts in markdown that are not a part of a tutorial
    ├── _containers/  # all posts in markdown that are a part of a tutorial
    ├── _templates/  # html templates
    ├── about/  # newcoder.io/about
    ├── contact/  # newcoder.io/contact
    ├── tutorials/  # newcoder.io/tutorials
    ├── api/  # newcoder.io/api
    ├── begin/  # newcoder.io/begin
    ├── dataviz/  # newcoder.io/dataviz
    ├── gui/  # newcoder.io/gui
    ├── networks/  # newcoder.io/networks
    ├── scrape/  # newcoder.io/scrape
    ├── workshop/  # newcoder.io/workshop
    ├── config.yml  # mynt configuration
    ├── index.html  # main landing page
    ├── requirements.txt  # requirements for running newcoder.io locally
    └── _local.sh  # mynt script to run newcoder.io locally
```

### Setup

```bash
$ git clone https://github.com/econchick/new-coder.git
```

#### For the website

```
$ cd new-coder/website
$ mkvirtualenv newcoder-website
(newcoder-website) $ pip install -r requirements.txt
# generate html files
(newcoder-website) $ mynt gen -f _site
# serve html files locally
(newcoder-website) $ mynt serve _site -p 5000
# now navigate to localhost:5000
# press CTRL+C to end
# or use the script to generate and serve
(newcoder-website) $ sh _local.sh
# now navigate to localhost:5000
# press CTRL+C to end

```

To re-generate html files automatically with each new save changed:

```bash
(newcoder-website) $ pwd
~/new-coder/website
(newcoder-website) $ mynt gen -f _site
(newcoder-website) $ pip install twisted
# in one shell/session:
(newcoder-website) $ twistd -n web --path _site --port 5000
# in another shell/session
(newcoder-website) $ pwd
~/new-coder/website
(newcoder-website) $ mynt watch _site
# navigate to localhost:5000
# CTRL+C in both shells to end
```

[newcoder.io](http://newcoder.io) is a static website. All the tutorial language is written in [Markdown](http://en.wikipedia.org/wiki/Markdown) within `new-coder/website/_posts`.  The HTML files are generated from Markdown using [mynt](http://mynt.mirroredwhite.com/).

### Website issues

Typo? Something unclear? Submit an issue, or fork this repository, make the fix, then submit a pull request.

To submit an issue, navigate [here](https://github.com/econchick/new-coder/issues/new) and give as much detail as possible.

To make the fix yourself:

1. You’ll need a GitHub account.
2. [Fork](https://github.com/econchick/new-coder/fork) the repository to your account.
3. `git clone $URL` where the $URL is your *own* fork URL here:

	![github fork url](http://dl.dropboxusercontent.com/s/zgdnm7fi2oey161/2013-08-18%20at%202.40%20PM.png)

4. Be sure to test your setup with the [setup](#setup) above.
5. Make necessary changes locally on your machine.  Note: make the changes within `website/_posts/` directory to the Markdown files, not the HTML files within `website/_site` (the `_site` directory is made when you run `mynt gen -f _site`).
6. Commit your changes, then push your changes to *your* fork.
7. Submit a pull request through GitHub’s [website](https://github.com/econchick/new-coder/compare/).  Be sure to give as much detail as possible in the title/description area.  Refer to an [issue number](https://github.com/econchick/new-coder/issues?state=open) if there is one.
8. I will receive an email.  If it’s been over a week or so and no response, go ahead and ping me via the pull request comments, or in an [email](mailto:lynn+github@newcoder.io).


### Tutorial code issues

Is there a typo in the code? Want to add clarity?  Found an error? Submit an issue, or fork this repository, make the fix, then submit a pull request.

To submit an issue, navigate [here](https://github.com/econchick/new-coder/issues/new) and give as much detail as possible.

To make the fix yourself:

1. You’ll need a GitHub account.
2. [Fork](https://github.com/econchick/new-coder/fork) the repository to your account.
3. `git clone $URL` where the $URL is your *own* fork URL here:

	![github fork url](http://dl.dropboxusercontent.com/s/zgdnm7fi2oey161/2013-08-18%20at%202.40%20PM.png)

4. `cd` into the tutorial that needs the fix, create a virtualenv, and run `pip install -r requirements.txt`.
5.  Make the necessary changes locally and update any documentation on the website with the [directions above](#website-issues).
6. Commit your changes, then push your changes to *your* fork.
7. Submit a pull request through GitHub’s [website](https://github.com/econchick/new-coder/compare/).  Be sure to give as much detail as possible in the title/description area.  Refer to an [issue number](https://github.com/econchick/new-coder/issues?state=open) if there is one.
8. I will receive an email.  If it’s been over a week or so and no response, go ahead and ping me via the pull request comments, or in an [email](mailto:lynn+github@newcoder.io).


### Suggestions, new features, new tutorials

Have a suggestion to improve newcoder.io? Submit an idea through [GitHub issues](https://github.com/econchick/new-coder/issues/new)!

Perhaps a new feature? or have an idea for another tutorial? Submit it through [GitHub](https://github.com/econchick/new-coder/issues/new) or shoot me an [email](mailto:lynn+github@newcoder.io)


### Helping our new coders

There is a very inactive IRC channel: #newcoder on Freenode.  I’d love it if mentors could hang out there!

Have an idea to give better support?  Let’s here it: submit an idea through [GitHub issues](https://github.com/econchick/new-coder/issues/new).

What I’m thinking about is a few things:

1. Mailing list
2. Discussion forum (perhaps with http://moot.it), similar to [PyLadies forum](http://discuss.pyladies.com).
3. Comment system within each of the steps/chapters


### ToDos

Beyond what is listed in the [open issues](https://github.com/econchick/new-coder/issues?state=open):

* Move [network tutorial](http://newcoder.io/~drafts/networks/) from “draft” mode to final.  This requires the tutorial itself to be reviewed for accuracy, readability, etc.
* Write the language behind the [gui](https://github.com/econchick/new-coder/tree/master/gui) tutorial.
* Implementing some sort of discussion ability to help out new coders, either with a mailing list, discussion forum, or commenting system.
* Improve design of site for general readability (e.g. the CSS).
* Add more “Extended” portions of each tutorial, maybe with more instruction or in general more helpful sites.

Go ahead and tackle any/all of these if you wish with a pull request!

Questions about contributing? [Email me](mailto:lynn+github@newcoder.io).
