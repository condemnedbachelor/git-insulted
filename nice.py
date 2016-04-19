from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'hygenically-challenged mole rat', 'dump heap', 'God-fearing failure', 'monstrosity', 'disgusting human being', 'wowza', 'oh-so-not-meh',
    'animalistic creep', 'genuinely pathetic moron', 'horse face', 'tubthumping idiot', 'inebriated mess', 'undeserving monster', 'terrible person']


@app.route('/')
def start_here():
    """Home page."""

    return "Hi! This is the home page. <a href='/hello'>Click here to Hello</a>"


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/diss">
          <label>What's your name? <input type="text" name="person"></label>
<!--           Select an insult: 
          <select name="insults">
            <option value ="hygenically-challenged-mole-rat">hygenically-challenged mole rat</option>
            <option value ="dump-heap">dump heap</option>            
            <option value ="God-fearing-failure">God-fearing failure</option>
            <option value ="monstrosity">monstrosity</option>
            <option value ="disgusting-human-being">disgusting human being</option>
            <option value ="animalistic-creep">animalistic creep</option>
            <option value ="genuinely-pathetic-moron">genuinely pathetic moron</option>            
            <option value ="horse-face">horse face</option>
            <option value ="tubthumping-idiot">tubthumping idiot</option>
            <option value ="inebriated-mess">inebriated mess</option>                      
            <option value ="undeserving-monster">undeserving monster</option>  
            <option value ="terrible-person">terrible person</option> 
          </select>                            -->        
          <input type="submit">
        </form>
      </body>
    </html>
    """


@app.route('/diss')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    insult = choice(AWESOMENESS)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment (heh)</title>
      </head>
      <body>
       <h1> ************************************************************************************<br>
        Listen, no offense, but I think %s is a great name for a %s. Your parents did well.<br>
        ************************************************************************************</h1>
      </body>
    </html>
    """ % (player, insult)




if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
