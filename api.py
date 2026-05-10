from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import random
import os

quotes = [
    {
        "quoteText": "You know, Hobbes, some days even my lucky rocket ship underpants don't help.",
        "quoteAuthor": "Calvin"
    },
    {
        "quoteText": "What a stupid world",
        "quoteAuthor": "Calvin"
    },
    {
        "quoteText": "Everybody seeks happiness! Not me, though! That's the difference between me and the rest of the world. Happiness isn't good enough for me! I demand euphoria!",
        "quoteAuthor": "Calvin"
    },
    {
        "quoteText": "I think night time is dark so you can imagine your fears with less distraction.",
        "quoteAuthor": "Calvin"
    },
    {
        "quoteText": "As you can see, I have memorized this utterly useless piece of information long enough to pass a test question. I now intend to forget it forever. You've taught me nothing except how to cynically manipulate the system. Congratulations.",
        "quoteAuthor": "Calvin"
    },
    {
        "quoteText": "Van Gogh would've sold more than one painting if he'd put tigers in them.",
        "quoteAuthor": "Hobbes"
    },
    {
        "quoteText": "The world bores you when you're cool.",
        "quoteAuthor": "Calvin"
    },
    {
        "quoteText": "Isn't it strange that evolution would give us a sense of humour? When you think about it, it's weird that we have a physiological response to absurdity. We laugh at nonsense. We like it. We think it's funny. Don't you think it's odd that we appreciate absurdity? Why would we develop that way? How does it benefit us?",
        "quoteAuthor": "Calvin"
    },
    {
        "quoteText": "I suppose if we couldn't laugh at things that don't make sense, we couldn't react to a lot of life. I can't tell if that's funny or really scary.",
        "quoteAuthor": "Hobbes and Calvin"
    },
    {
        "quoteText": "Life is full of surprises, but never when you need one.",
        "quoteAuthor": "Calvin"
    },
    {
        "quoteText": "Getting an inch of snow is like winning 10 cents in the lottery.",
        "quoteAuthor": "Calvin"
    },
    {
        "quoteText": "People always make the mistake of thinking art is created for them. But really, art is a private language for sophisticates to congratulate themselves on their superiority to the rest of the world. As my artist's statement explains, my work is utterly incomprehensible and is therefore full of deep significance.",
        "quoteAuthor": "Calvin"
    },
    {
        "quoteText": "Verbing weirds language.",
        "quoteAuthor": "Calvin"
    },
    {
        "quoteText": "They say the world is a stage. But obviously the play is unrehearsed and everybody is ad-libbing his lines.Maybe that's why it's hard to tell if we're living in a tragedy or a farce.We need more special effects and dance numbers.",
        "quoteAuthor": "Calvin and Hobbes"
    },
    {
        "quoteText": "Sometimes I think the surest sign that intelligent life exists elsewhere in the universe is that none of it has tried to contact us.",
        "quoteAuthor": "Calvin"
    },
    {
        "quoteText": "So the secret to good self-esteem is to lower your expectations to the point where they're already met?",
        "quoteAuthor": "Hobbes"
    },
    {
        "quoteText":"Becoming an adult is probably the dumbest thing you could ever do",
        "quoteAuthor":"Calvin"
    },
    {
        "quoteText":"How old do you have to be before you know what's going on?",
        "quoteAuthor":"Calvin"
    },
    {
        "quoteText":"Know what's weird? Day to day nothing seems to change, but pretty soon everything is different.",
        "quoteAuthor":"Calvin"
    },
    {
        "quoteText":"Your denial of my victimhood is lowering my self esteem!",
        "quoteAuthor":"Calvin"
    },
    {
        "quoteText":"Given that sooner or later, we're all just going to die, what's the point of learning about integers?",
        "quoteAuthor":"Calvin"
    },
    {
        "quoteText":"You just go about your business and one day you realize you're not the same person you used to be. People change whether they decide to or not!",
        "quoteAuthor":"Calvin"
    },
    {
        "quoteText":"Do you think our morality is defined by our actions, or by what’s inside our hearts?",
        "quoteAuthor":"Calvin"
    },
    {
        "quoteText":"Isn't it sad how some people's grip on their lives is so precarious that they'll embrace any preposterous delusion, rather than face an occasional bleak truth?",
        "quoteAuthor":"Calvin"
    },
    {
        "quoteText":"If you care, you just get disappointed all the time. If you don't care, nothing matters. So you're never upset.",
        "quoteAuthor":"Calvin"
    },
    {
        "quoteText":"Change is invigorating! If you don't accept new challenges you become complacent and lazy. Your life atrophies!",
        "quoteAuthor":"Calvin"
    },
    {
        "quoteText":"If people sat outside and looked at the stars each night, I'll bet they'd live a lot differently.",
        "quoteAuthor":"Calvin"
    },
    {
        "quoteText":"We seem to understand the value of oil, timber, minerals and housing, but not the value of unspoiled beauty, wildlife, solitude and spiritual renewal.",
        "quoteAuthor":"Calvin"
    },
    {
        "quoteText":"I try to make everyone's day a little more surreal.",
        "quoteAuthor":"Calvin"
    },
    {
        "quoteText":"I don't care about issues! I've got better things to do than argue with every wrongheaded crackpot with an ignorant opinion! I'm a busy man.",
        "quoteAuthor":"Calvin"
    },
    {
        "quoteText":"Why does the universe always give you the sign after you do it?",
        "quoteAuthor":"Calvin"
    },
    {
        "quoteText":"Great experiences are even better when they're shared.",
        "quoteAuthor":"Calvin"
    },
    {
        "quoteText":"When a person pauses in mid-sentence to choose a word, that's the best time to jump in and change the subject.",
        "quoteAuthor":"Calvin"
    },
    {
        "quoteText":"Nothing is permanent, everything changes. That's the one thing we know for sure in this world.",
        "quoteAuthor":"Calvin"
    },
    {
        "quoteText":"I find my life is easier the lower I keep everyone's expectations.",
        "quoteAuthor":"Calvin"
    },
    {
        "quoteText":"What on earth am I doing in here on this beautiful day? This is the only life I've got!",
        "quoteAuthor":"Calvin"
    },
    {
        "quoteText":"I tell you Hobbes, it's great to have a friend who appreciates an earnest discussion of ideas.",
        "quoteAuthor":"Calvin"
    },
    {
        "quoteText":"We hurl through an incomprehensible darkness. In cosmic terms, we are subatomic particles in a grain of sand on an infinite beach.",
        "quoteAuthor":"Calvin"
    },
    {
        "quoteText":"There's never enough time to do all the nothing you want.",
        "quoteAuthor":"Calvin"
    },
    {
        "quoteText":"Here I am, waiting for the bus. Eleven more years of school to go. Then college, then maybe graduate school, and then I work until I die.",
        "quoteAuthor":"Calvin"
    },
    {
        "quoteText":"It's a hard, bitter, cruel world to have to grow up in, Hobbes.",
        "quoteAuthor":"Calvin"
    },
    {
        "quoteText":"Isn't it weird that one's own past can seem unreal? This is like looking at a picture of someone else.",
        "quoteAuthor":"Calvin"
    },
    {
        "quoteText":"Oh greatest of the mass media, thank you for elevating emotion, reducing thought, and stifling imagination.",
        "quoteAuthor":"Calvin"
    },
    {
        "quoteText":"I must say, the future is quite a bit different than I expected.",
        "quoteAuthor":"Calvin"
    },
    {
        "quoteText":"Sometimes I think the surest sign that intelligent life exists elsewhere in the universe is that none of it has tried to contact us.",
        "quoteAuthor":"Calvin"
    },
    {
        "quoteText":"It offends the human ego that nature is indifferent to us.",
        "quoteAuthor":"Calvin"
    },
    {
        "quoteText":"Ya know, sometimes the world seems like a pretty mean place.",
        "quoteAuthor":"Calvin"
    },
    {
        "quoteText":"A day can really slip by when you're deliberately avoiding what you're supposed to do.",
        "quoteAuthor":"Calvin"
    },
    {
        "quoteText":"I like to experience life to the fullest. I say you don't fully appreciate life until you risk losing it.",
        "quoteAuthor":"Calvin"
    },
    {
        "quoteText":"I wondered, is it better to do the right thing and fail or is it better to do the wrong thing and succeed?",
        "quoteAuthor":"Calvin"
    },
    {
        "quoteText":"Did you ever wonder if the person in the puddle is real, and you're just a reflection of him?",
        "quoteAuthor":"Calvin"
    },
    {
        "quoteText":"Given the pace of technology, I propose we leave math to the machines and go play outside.",
        "quoteAuthor":"Calvin"
    },
    {
        "quoteText":"If good things lasted forever, would we appreciate how precious they are?",
        "quoteAuthor":"Hobbes"
    },
    {
        "quoteText":"I suppose if we couldn't laugh at things that don't make sense, we couldn't react to a lot of life.",
        "quoteAuthor":"Hobbes"
    },
    {
        "quoteText":"Is it a right to remain ignorant?",
        "quoteAuthor":"Hobbes"
    },
    {
        "quoteText":"If you couldn't find any weirdness, maybe we'll just have to make some.",
        "quoteAuthor":"Hobbes"
    },
    {
        "quoteText":"If people could put rainbows in zoos, they'd do it!",
        "quoteAuthor":"Hobbes"
    },
    {
        "quoteText":"Somehow, it's always right now until it's later.",
        "quoteAuthor":"Hobbes"
    },
    {
        "quoteText":"Sometimes one should just look at things and think about things, without doing things.",
        "quoteAuthor":"Hobbes"
    },
    {
        "quoteText":"I think our actions show what's inside our hearts.",
        "quoteAuthor":"Hobbes"
    }
]


app = Flask(__name__, static_folder='static')
CORS(app)

@app.route('/')
def index():
    with open('index.html', 'r') as f:
        return f.read(), 200, {'Content-Type': 'text/html'}

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename) 

@app.route('/assets/<path:filename>')
def assets(filename):
    return send_from_directory('assets', filename)

def generate_random_quote():
    quote = random.choice(quotes)
    return jsonify(quote)

#the json will run on "http://127.0.0.1:8080"
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
