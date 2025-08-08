import os
from http.server import HTTPServer

PORT = int(os.environ.get("PORT", 8080))

# your handler code above...
server_address = ("0.0.0.0", PORT)
httpd = HTTPServer(server_address, MyHandler)
print(f"Serving on port {PORT}...")
httpd.serve_forever()


quotes_by_mood = {
    "😊": [
        "Happiness comes from within.",
    "Gratitude turns what we have into enough.",
    "Every day may not be good, but there's something good in every day.",
    "The more you smile, the more life smiles back at you.",
    "Joy is a decision, not a reaction.",
    "Focus on what you have, not what you lack.",
    "Life is better when you laugh.",
    "Start each day with a grateful heart.",
    "A happy heart makes a bright face.",
    "Your vibe attracts your tribe.",
    "Find joy in the little things.",
    "Positivity is contagious.",
    "The best time for happiness is now.",
    "Happiness is homemade.",
    "The secret to having it all is knowing you already do.",
    "Choose joy, no matter the circumstance.",
    "Good vibes only.",
    "Smiles are free but worth a lot.",
    "Happiness looks good on you.",
    "Gratitude is the best attitude.",
    "Happiness is an inside job.",
    "Find reasons to laugh every day.",
    "Every moment matters—enjoy it.",
    "The happier you are, the more beauty you see.",
    "Happiness is found in the present moment.",
    "Live in the sunshine.",
    "Laughter is timeless.",
    "Your happiness is your responsibility.",
    "Happiness grows when shared.",
    "Enjoy the little detours.",
    "A grateful mind is a happy mind.",
    "Smile more, worry less.",
    "Collect moments, not things.",
    "Happiness is a habit—cultivate it.",
    "Kindness fuels happiness.",
    "Dance like nobody’s watching.",
    "Happiness is free—spend it generously.",
    "Happiness blooms from within.",
    "Every smile makes the world brighter.",
    "Radiate positivity.",
    "Happiness begins with gratitude.",
    "Contentment is the true wealth.",
    "Happiness is being yourself.",
    "Enjoy today for it will never come again.",
    "Gratitude makes what we have enough.",
    "A cheerful heart is good medicine.",
    "Happiness doesn’t need a reason.",
    "Joy is a daily choice.",
    "Choose to see the good.",
    "The smallest joy can change a day.",
    "Be happy for no reason.",
    "Happiness comes from giving.",
    "Make happiness your priority.",
    "Happiness is homemade, not store-bought.",
    "Cherish every sunrise and sunset.",
    "Your smile is your logo.",
    "Find beauty in every day.",
    "Happiness starts with a smile.",
    "Happiness is loving what you have.",
    "Live joyfully in the present.",
    "Happiness is enjoying the simple things.",
    "Happiness is waking up with a purpose.",
    "A happy soul is the best shield.",
    "Happiness is a choice we make every morning.",
    "The happiest people focus on what they can control.",
    "Joy multiplies when shared.",
    "Be happy—it drives people crazy.",
    "Happiness is the path, not the destination.",
    "Happiness is a warm cup of tea.",
    "Gratitude opens the door to happiness.",
    "Happiness grows in a kind heart.",
    "Your joy is your power.",
    "Happiness is contagious—spread it.",
    "Stay close to what makes you feel alive.",
    "Happiness is a journey you create.",
    "The key to happiness is letting go.",
    "Happiness comes when you stop comparing.",
    "Fill your day with sunshine.",
    "Happiness is found in the simplest moments.",
    "Happiness is in the now.",
    "Celebrate small victories.",
    "Happiness is peace of mind.",
    "Smiling is the best makeup.",
    "Happiness is found when you help others.",
    "Happiness is free—claim it.",
    "Happiness is found in acts of kindness.",
    "Happiness is knowing you matter.",
    "Happiness is a grateful heart.",
    "Be the reason someone smiles today.",
    "Happiness is believing in yourself.",
    "Happiness comes from loving fully.",
    "Happiness is seeing others happy.",
    "Happiness is a warm embrace.",
    "Happiness is waking up without regrets.",
    "Happiness is making the most of today.",
    "Happiness is being at peace with yourself.",
    "Happiness is a choice, not a result.",
    "Happiness is enjoying life as it is.",
    "Happiness is finding joy in the present moment."
    ],
    "😢": [
        "This too shall pass.",
    "The sun will rise and we will try again.",
    "Every storm eventually runs out of rain.",
    "Better days are coming.",
    "One day you will tell your story of how you overcame what you went through.",
    "You are stronger than you think.",
    "Even the darkest night will end and the sun will rise.",
    "Your current situation is not your final destination.",
    "Healing takes time—be patient with yourself.",
    "It’s okay to not be okay.",
    "You have survived 100% of your worst days.",
    "The pain you feel today will be the strength you feel tomorrow.",
    "You are not alone in this.",
    "Storms make trees take deeper roots.",
    "Sometimes the bad times put us on the path to the best times.",
    "Be gentle with yourself; you’re doing the best you can.",
    "Your feelings are valid.",
    "One step at a time is still progress.",
    "Courage doesn’t always roar—sometimes it’s the quiet voice that says ‘I will try again tomorrow.’",
    "It’s okay to ask for help.",
    "The greatest oak was once a little nut that held its ground.",
    "Keep going, no matter how slow.",
    "Your struggle is part of your story.",
    "Tough times never last, but tough people do.",
    "Fall seven times and stand up eight.",
    "Small steps forward are still steps forward.",
    "You are allowed to rest.",
    "Scars are proof you are stronger than what tried to hurt you.",
    "Your value doesn’t decrease because of a setback.",
    "Rainy days make flowers grow.",
    "You are allowed to outgrow the things that no longer serve you.",
    "Your comeback will be greater than your setback.",
    "You don’t have to have it all figured out to move forward.",
    "Breathe—this moment will pass.",
    "You have permission to heal at your own pace.",
    "Even the longest winter turns to spring.",
    "Don’t let a bad day make you feel like you have a bad life.",
    "You are more than your mistakes.",
    "Keep your head up; your heart will follow.",
    "Every day you choose to continue is a victory.",
    "You’re doing better than you think.",
    "Be proud of yourself for how far you’ve come.",
    "You are allowed to let go of what hurts you.",
    "You will smile again.",
    "Sometimes you just need to rest and let the world turn without you for a bit.",
    "You don’t have to be strong all the time.",
    "Some of the best chapters in life start with a sad page.",
    "You’re not broken—you’re healing.",
    "Pain is temporary; growth is permanent.",
    "Even the smallest light can brighten the darkest night.",
    "Your heart will feel light again.",
    "It’s okay to cry—it’s a sign of strength.",
    "You are not your past.",
    "Your worth is not defined by your struggles.",
    "One day you’ll look back and see how far you’ve come.",
    "You can be a masterpiece and a work in progress at the same time.",
    "You deserve love, even on your worst days.",
    "Every day you keep going is a success.",
    "You’ve overcome so much already.",
    "The world is better with you in it.",
    "You will find peace again.",
    "It’s okay to start over.",
    "You have nothing to prove to anyone.",
    "Even the smallest step forward is progress.",
    "Every ending is a new beginning.",
    "You’re not a burden—you’re a human being with feelings.",
    "It’s not weak to admit you’re hurting.",
    "Sometimes strength looks like asking for help.",
    "You don’t have to pretend to be okay.",
    "Your future needs you—your past does not.",
    "It’s okay to take life one breath at a time.",
    "The weight you carry will get lighter.",
    "You are more than what happened to you.",
    "You have every right to be here.",
    "Your feelings matter.",
    "Be patient with yourself—you are growing.",
    "It’s okay to set boundaries to protect your peace.",
    "Time will heal the wounds you thought would never fade.",
    "You can survive this storm.",
    "You’re allowed to be proud of surviving.",
    "You will not feel this way forever.",
    "It’s okay to find joy again after sadness.",
    "You are allowed to grieve and still move forward.",
    "The best views come after the hardest climbs.",
    "Every scar tells a story of survival.",
    "Your presence matters.",
    "You are more capable than you realize.",
    "Pain is part of life, but so is joy.",
    "You deserve rest and kindness.",
    "You are not weak for feeling deeply.",
    "You are not alone in this fight.",
    "The sun always shines again.",
    "Your journey is not over.",
    "Better days are on their way.",
    "You deserve to feel safe and loved.",
    "Keep choosing to live, even when it’s hard.",
    "Your story is not finished yet.",
    "You are enough, just as you are.",
    "One day the pain will make sense.",
    "You can still be happy again."
    ],
    "😡": [
        "Control your anger before it controls you.",
    "Don’t let anger make your decisions.",
    "A moment of patience can save a lifetime of regret.",
    "When angry, pause before you speak.",
    "Not every action deserves a reaction.",
    "Walk away, not out of weakness, but out of strength.",
    "Your peace is worth more than your pride.",
    "Calm minds win battles.",
    "Silence is often the best reply to anger.",
    "Choose to respond, not react.",
    "He who angers you, controls you.",
    "Breathe in peace, breathe out anger.",
    "Don’t trade your peace for someone else’s chaos.",
    "Strong people control their emotions.",
    "Step back before you strike back.",
    "Don’t burn bridges with words spoken in anger.",
    "Rise above the heat of the moment.",
    "Your calmness is your power.",
    "Anger is a fire—don’t let it consume you.",
    "Sometimes the best revenge is no revenge at all.",
    "Don’t feed the fire of your frustration.",
    "Hold your tongue until your heart is calm.",
    "Keep your dignity even when others lose theirs.",
    "Peace is power.",
    "Let go of what you can’t control.",
    "Control the controllable—ignore the rest.",
    "Don’t waste energy on people who drain you.",
    "Your focus determines your reality.",
    "The calmer you are, the clearer you think.",
    "Don’t let temporary emotions make permanent decisions.",
    "Stay cool under pressure.",
    "Anger clouds judgment—clarity comes with calm.",
    "Self-control is a form of strength.",
    "Sometimes the smartest move is no move.",
    "Think twice, speak once, regret never.",
    "Don’t let a bad moment ruin your day.",
    "Keep your heart soft but your boundaries strong.",
    "Let the storm pass before you act.",
    "Don’t react immediately—wait until the emotion fades.",
    "Your peace is your biggest victory.",
    "Never let someone’s actions dictate your character.",
    "Speak only when your words improve the silence.",
    "An angry mind is a weak mind.",
    "Stay silent until you can speak with intention.",
    "The one who stays calm is the strongest in the room.",
    "Be like water—adaptable and calm.",
    "Detach, don’t engage.",
    "Pause before you punish.",
    "Keep calm, even if the world burns around you.",
    "Choose peace over proving a point.",
    "Don’t wrestle with pigs; you both get dirty.",
    "Energy flows where attention goes—don’t give anger attention.",
    "A calm mind is a powerful mind.",
    "Don’t lose yourself in the heat of the moment.",
    "Slow down before you explode.",
    "Sometimes the best answer is to walk away.",
    "Your silence can speak louder than your anger.",
    "Stay centered when everything around you is spinning.",
    "You can’t control others, but you can control yourself.",
    "Don’t let pride fuel your rage.",
    "Revenge wastes your energy—use it to grow instead.",
    "Don’t react to provocation; rise above it.",
    "Anger fades when ignored.",
    "Your reaction is your responsibility.",
    "A controlled tongue is a sign of strength.",
    "Turn your anger into ambition.",
    "Use anger as fuel, not fire.",
    "Your calm is your superpower.",
    "Anger is loud, but calm is heard.",
    "Don’t let anger close your mind.",
    "When provoked, smile instead.",
    "Disarm anger with patience.",
    "Count to ten before responding.",
    "Peace frustrates those who want conflict.",
    "If it costs you peace, it’s too expensive.",
    "Protect your mental space from negativity.",
    "Not reacting is a reaction too.",
    "A quick temper leaves a long trail of damage.",
    "Think of the outcome before you act.",
    "Hold your fire until your aim is clear.",
    "Some battles aren’t worth fighting.",
    "Stay calm—it confuses your enemies.",
    "Anger is temporary—don’t let it do permanent damage.",
    "Don’t let small things steal your big peace.",
    "React with thought, not emotion.",
    "An angry word is like a stone—you can’t take it back.",
    "You win when you refuse to fight.",
    "The quieter you are, the more you hear.",
    "Keep your mind cool in heated moments.",
    "Let them be loud—you be still.",
    "Turn frustration into focus.",
    "Patience is a shield against anger.",
    "The less you respond to negativity, the more peaceful you become.",
    "Don’t add fuel to the fire.",
    "Stay calm—it’s the ultimate revenge.",
    "Walk away for your own peace of mind.",
    "Your inner peace is more valuable than proving you’re right.",
    "Choose calm over chaos every time."
    ],
    "😴": [
        "Rest is part of the process.",
    "You can’t pour from an empty cup.",
    "Sometimes the most productive thing you can do is rest.",
    "Take a break, not a surrender.",
    "Your body needs rest as much as it needs movement.",
    "Slow down before life forces you to.",
    "Rest now so you can rise later.",
    "Even the sun sets to rest.",
    "A well-rested mind thinks clearer.",
    "Recharge and try again tomorrow.",
    "It’s okay to stop for a while.",
    "Rest is the key to longevity.",
    "Balance is better than burnout.",
    "The pause is as important as the play.",
    "Sometimes you need to do nothing to heal everything.",
    "Take a breath—this moment matters.",
    "Even the strongest need rest.",
    "Your worth isn’t measured by your exhaustion.",
    "Tired minds make poor decisions—rest first.",
    "Rest is medicine.",
    "Give yourself permission to rest.",
    "You are not lazy for taking a break.",
    "A rested soul is a creative soul.",
    "Rest today to be stronger tomorrow.",
    "You can’t be your best when you’re running on empty.",
    "Pause, breathe, restore.",
    "Sleep is an investment in tomorrow.",
    "Rest brings clarity.",
    "Sometimes, doing nothing is doing something important.",
    "Your body whispers for rest before it screams.",
    "The best ideas come when the mind is calm.",
    "You can’t hustle if you’re broken.",
    "Rest allows your soul to catch up with your body.",
    "Even machines need downtime.",
    "Rest is how you rebuild your strength.",
    "You deserve to rest without guilt.",
    "Tired? That’s your body asking for care.",
    "Don’t mistake rest for weakness.",
    "Without rest, work loses its quality.",
    "Recovery is part of the journey.",
    "Rest is essential, not optional.",
    "Take time to refill your energy.",
    "Listen to your body’s need for rest.",
    "Sleeping well is self-respect.",
    "Rest resets your perspective.",
    "Don’t run faster than your soul can go.",
    "When tired, learn to rest, not quit.",
    "A good night’s sleep is a superpower.",
    "Your body heals when you rest.",
    "Take the rest you’ve earned.",
    "The pause is where growth begins.",
    "Rest prevents collapse.",
    "The world can wait while you rest.",
    "Fatigue is a sign to slow down.",
    "Stop before you crash.",
    "Rest is fuel for your dreams.",
    "Even nature rests between seasons.",
    "Sleep is the best meditation.",
    "Honor your need for rest.",
    "A rested you is a better you.",
    "Sometimes you need stillness to move forward.",
    "Rest is strength in disguise.",
    "Time spent resting is never wasted.",
    "The more you rest, the more you can give.",
    "You’re allowed to unplug.",
    "Rest so you can rise refreshed.",
    "Don’t fight the need for rest.",
    "Rest allows your mind to focus.",
    "Sleep well, live well.",
    "A calm mind comes from a rested body.",
    "Your energy is precious—protect it.",
    "Nothing works without rest.",
    "Rest is part of self-care.",
    "Without rest, passion fades.",
    "Rest now or regret later.",
    "Rest to be your best.",
    "Sometimes you need to pause to keep going.",
    "Don’t wait until you’re too tired to rest.",
    "The body thrives on rhythm—work and rest.",
    "Take time to restore your energy.",
    "Rest is the foundation of productivity.",
    "Pause to appreciate how far you’ve come.",
    "Your dreams grow when you sleep.",
    "Good rest leads to good work.",
    "You don’t have to earn rest.",
    "Rest is how you recover your spark.",
    "Burnout is what happens when you ignore rest.",
    "Rest is an act of self-love.",
    "Tiredness is a signal, not a flaw.",
    "The more you rest, the better you perform.",
    "Make space for quiet in your life.",
    "True rest is a necessity, not a luxury.",
    "Rest is how you heal the unseen wounds.",
    "A day of rest is a day of growth.",
    "Rest is preparation for what’s ahead.",
    "Allow yourself moments of stillness.",
    "Sometimes the bravest thing you can do is rest.",
    "Peace begins with rest.",
    "The future is brighter when you are rested."
    ],
    "😎": [
        "Believe you can and you’re halfway there.",
    "Success starts with self-belief.",
    "Your only limit is your mind.",
    "Act like the person you want to become.",
    "Confidence is silent, insecurities are loud.",
    "Doubt kills more dreams than failure ever will.",
    "Don’t wait for opportunity—create it.",
    "You are capable of amazing things.",
    "Be so good they can’t ignore you.",
    "Fortune favors the bold.",
    "Dream big, work hard, stay focused.",
    "Confidence is preparation.",
    "No one is you, and that’s your power.",
    "Push yourself, because no one else will do it for you.",
    "Great things never come from comfort zones.",
    "Your dreams are worth the risk.",
    "Winners focus on winning, losers focus on winners.",
    "Be fearless in the pursuit of what sets your soul on fire.",
    "Success is the sum of small efforts repeated daily.",
    "Stand tall, even when you feel small.",
    "Success begins at the end of your comfort zone.",
    "You don’t need permission to be great.",
    "Be your own biggest fan.",
    "Your confidence intimidates those with none.",
    "Stay hungry, stay foolish.",
    "Fear is temporary—regret is forever.",
    "Take the risk or lose the chance.",
    "Your potential is endless.",
    "Act as if it were impossible to fail.",
    "Work until your idols become your rivals.",
    "If you want it, go get it.",
    "The best way to predict the future is to create it.",
    "Keep going until your bank account looks like your phone number.",
    "Stay focused and extra sparkly.",
    "Hustle until you no longer have to introduce yourself.",
    "You are the CEO of your life.",
    "Success is built on consistency.",
    "Be a voice, not an echo.",
    "Prove yourself to yourself, not to others.",
    "Be stronger than your excuses.",
    "Never stop learning and growing.",
    "Your confidence can change the room.",
    "If you want different results, take different actions.",
    "Small progress is still progress.",
    "Don’t just talk about it—be about it.",
    "You didn’t come this far to only come this far.",
    "Work for it more than you hope for it.",
    "Success loves speed.",
    "Be the energy you want to attract.",
    "You have to believe before you achieve.",
    "Start before you’re ready.",
    "Ambition is the path to success.",
    "No pressure, no diamonds.",
    "The comeback is always stronger than the setback.",
    "Be obsessed with your goals.",
    "Confidence is the best outfit—wear it daily.",
    "Decide, commit, succeed.",
    "Stay consistent, success will follow.",
    "Your future self will thank you.",
    "Never underestimate the power of self-belief.",
    "Be unstoppable.",
    "Don’t wish for it—work for it.",
    "You are one decision away from a different life.",
    "Don’t be afraid to be the first.",
    "If they can do it, so can you.",
    "Keep your eyes on the prize.",
    "Outwork your yesterday.",
    "The grind will pay off.",
    "Success requires discipline.",
    "You can and you will.",
    "Confidence attracts success.",
    "Every champion was once a beginner.",
    "Push past the fear.",
    "Don’t limit your challenges—challenge your limits.",
    "Rise up and attack the day with enthusiasm.",
    "Go the extra mile—it’s never crowded.",
    "Your energy introduces you before you speak.",
    "Focus on progress, not perfection.",
    "Do something today your future self will thank you for.",
    "Great minds think big.",
    "Be willing to do what others won’t.",
    "The harder you work, the luckier you get.",
    "Success begins in the mind.",
    "Winners never quit.",
    "Don’t be afraid to stand out.",
    "Every step forward is a step closer.",
    "Make it happen.",
    "The best investment is in yourself.",
    "You are built for greatness.",
    "Confidence is contagious.",
    "Don’t stop until you’re proud.",
    "Stay disciplined when motivation fades.",
    "You are your greatest asset.",
    "Keep winning silently.",
    "Start small, dream big, grow fast.",
    "Be the reason you succeed.",
    "Take action, not just notes.",
    "If you can dream it, you can do it.",
    "Create your own luck.",
    "Turn your can'ts into cans and your dreams into plans."
    ]
}



class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(self.html_page().encode("utf-8"))
        elif parsed.path == "/quote":
            params = urllib.parse.parse_qs(parsed.query)
            mood = params.get("mood", [""])[0]
            if mood in quotes_by_mood:
                quote = random.choice(quotes_by_mood[mood])
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"quote": quote}).encode("utf-8"))
            else:
                self.send_response(404)
                self.end_headers()
        else:
            # serve static files like the QR image if requested directly
            return super().do_GET()

    def html_page(self):
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Motivation</title>
<style>
  :root {{
    --fg: #fff;
    --muted: #cfd3dc;
  }}
  * {{ box-sizing: border-box; }}
  html, body {{
    margin: 0; height: 100%; overflow: hidden;
    background: #000; color: var(--fg);
    font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
  }}

  /* Center container (both axes) */
  #overlay {{
    position: absolute; inset: 0;
    display: grid;
    place-items: center;
    z-index: 10;
    padding: 1rem;
  }}
  /* Inner column so content stays centered & constrained */
  .stack {{
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    gap: clamp(.6rem, 2.2vw, 1rem);
    max-width: 980px; width: min(92vw, 980px);
    text-align: center;
  }}

  /* Emoji row */
  .emoji-row {{
    display: flex; flex-wrap: wrap; gap: clamp(.4rem, 2vw, .7rem);
    align-items: center; justify-content: center;
  }}

  /* Transparent emoji buttons, responsive size */
  .emoji-btn {{
    background: transparent; border: none; cursor: pointer;
    font-size: clamp(2rem, 7vw, 3.5rem);
    line-height: 1; padding: .25rem .35rem;
    border-radius: 14px;
    transition: transform .15s ease, background-color .2s ease;
  }}
  .emoji-btn:hover {{ transform: scale(1.06); background-color: rgba(255,255,255,.06); }}
  .emoji-btn:active {{ transform: scale(.98); }}

  /* Quote & guidance text – responsive */
  #quote {{
    margin-top: .2rem;
    font-size: clamp(1.05rem, 2.6vw, 1.6rem);
    line-height: 1.35;
    max-width: 90ch;
  }}
  #guidance {{
    color: var(--muted);
    font-size: clamp(.95rem, 2.2vw, 1.1rem);
    line-height: 1.55;
    max-width: 90ch;
  }}
  #guidance h2 {{
    color: var(--fg); opacity: .9;
    margin: .2rem 0 .4rem; font-size: clamp(1rem, 2.2vw, 1.15rem);
  }}

  /* Tip section + address */
  .tip-panel {{
    display: grid; gap: .5rem; place-items: center;
  }}
  .btn {{
    padding: clamp(.55rem, 2.4vw, .8rem) clamp(.9rem, 3vw, 1.1rem);
    border-radius: 10px;
    border: 1px solid rgba(255,255,255,.15);
    background: rgba(255,255,255,.06);
    color: var(--fg); cursor: pointer; font-weight: 600;
    font-size: clamp(.95rem, 2.5vw, 1.05rem);
    transition: background .15s ease, transform .15s ease, border-color .15s ease;
  }}
  .btn:hover {{ background: rgba(255,255,255,.12); border-color: rgba(255,255,255,.25); transform: translateY(-1px); }}

  .addr {{
    display: flex; gap: .5rem; align-items: center; flex-wrap: wrap; justify-content: center;
    font-size: clamp(.85rem, 2.2vw, .95rem);
    opacity: .9;
  }}
  .copy-btn {{
    background: rgba(255,255,255,0.08); color: #fff;
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 8px; padding: .25rem .5rem; cursor: pointer;
    font-size: clamp(.8rem, 2vw, .9rem);
  }}

  /* QR image responsive & smaller on phones */
  #qr {{
    margin-top: .6rem;
    width: clamp(82px, 18vw, 120px);
    height: auto; cursor: pointer; opacity: .95;
  }}

  /* Footer */
  #footer {{
    margin-top: .2rem;
    font-size: clamp(.8rem, 2vw, .95rem);
    opacity: .8; max-width: 90ch; line-height: 1.4;
  }}

  /* Canvas fills background */
  #bg {{ position: fixed; inset: 0; width: 100%; height: 100%; display: block; }}
</style>
</head>
<body>
  <div id="overlay">
    <div class="stack">
      <div class="emoji-row">
        <button class="emoji-btn" onclick="sendMood('😊')" title="Happy/Grateful">😊</button>
        <button class="emoji-btn" onclick="sendMood('😢')" title="Sad/Struggling">😢</button>
        <button class="emoji-btn" onclick="sendMood('😡')" title="Angry/Frustrated">😡</button>
        <button class="emoji-btn" onclick="sendMood('😴')" title="Tired/Overwhelmed">😴</button>
        <button class="emoji-btn" onclick="sendMood('😎')" title="Confident/Ambitious">😎</button>
      </div>

      <div id="quote">Pick a mood to get inspired.</div>

      <div id="guidance">
        <h2>Guidance</h2>
        <div id="guidanceText">Pick a mood above to see practical guidance.</div>
      </div>

      <div class="tip-panel">
        <button class="btn" onclick="openPhantom()">Tip if you find it helpful</button>
        <div class="addr">
          <span>Solana Address:</span>
          <span id="walletAddr">FbXJRbGrfLxjSuncoRz2sjEyjtziey5mQ7hhRVXLhG22</span>
          <button class="copy-btn" onclick="copyAddr()">📋 Copy</button>
        </div>
        <img id="qr" src="1000018000.jpg" alt="QR Code" onclick="openPhantom()" />
      </div>

      <div id="footer">
        This website exists to inspire and guide you using timeless wisdom, practical psychology, and science-backed strategies for overcoming challenges.
      </div>
    </div>
  </div>

  <canvas id="bg"></canvas>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r134/three.min.js"></script>
  <script>
    // Guidance per mood
    const guidanceByMood = {{
      "😊": "Practice gratitude now: list three small wins from today. Share one compliment. Move your body for two minutes to anchor the feeling. Happiness compounds when you give it away—do one kind act before you close this page.",
      "😢": "Breathe box-style: 4 in, 4 hold, 4 out, 4 hold (3 rounds). Name your feeling without judging it. Text one person: “I’m having a rough day, can we talk later?” Take one small step—water, shower, or a 5-minute walk. This moment will pass.",
      "😡": "Pause before you respond. Do 10 slow breaths through the nose; exhale longer than inhale. Write the response you want to send—don’t send it for 30 minutes. Choose one fact-based action that improves your position tomorrow.",
      "😴": "Stop, downshift, and protect sleep. Choose one task only and time-box it to 15 minutes—then stop. Drink water, stretch your neck, and dim screens. Set a simple shutdown routine: list tomorrow’s top 3, then close the day.",
      "😎": "Clarify your target: one outcome, one metric, one next step. Start a 20-minute focus sprint now—no notifications. Ship something tiny today. Confidence follows evidence: stack a win you can complete before the hour ends."
    }};

    function sendMood(mood){{ 
      fetch(`/quote?mood=${{encodeURIComponent(mood)}}&t=${{Date.now()}}`)
        .then(res => res.json())
        .then(data => {{
          document.getElementById('quote').innerText = data.quote;
          speakQuote(data.quote);
          const g = guidanceByMood[mood] || "Act on what you can control. Start small. Start now.";
          document.getElementById('guidanceText').innerText = g;
          colorParticles(mood);
        }});
    }}

    function speakQuote(text){{ 
      const utter = new SpeechSynthesisUtterance(text);
      utter.lang = 'en-US';
      utter.pitch = 0.55;   // deeper
      utter.rate = 0.92;    // slightly slower
      const voices = speechSynthesis.getVoices();
      const pick = voices.find(v => /male|baritone|daniel|david|english/i.test(v.name)) || null;
      if (pick) utter.voice = pick;
      speechSynthesis.cancel();
      speechSynthesis.speak(utter);
    }}

    function copyAddr() {{
      const addr = document.getElementById('walletAddr').innerText.trim();
      navigator.clipboard.writeText(addr);
      alert("Address copied to clipboard!");
    }}

    function openPhantom() {{
      window.open('https://phantom.app/ul/browse/solana:transfer?address=FbXJRbGrfLxjSuncoRz2sjEyjtziey5mQ7hhRVXLhG22', '_blank');
    }}

    // Three.js particles background (responsive)
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({{canvas: document.getElementById("bg"), antialias: true}});
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.setSize(window.innerWidth, window.innerHeight);
    camera.position.z = 5;

    const particlesCount = 700;
    const geometry = new THREE.BufferGeometry();
    const posArray = new Float32Array(particlesCount * 3);
    for (let i = 0; i < particlesCount * 3; i++) {{
      posArray[i] = (Math.random() - 0.5) * 12;
    }}
    geometry.setAttribute('position', new THREE.BufferAttribute(posArray, 3));
    const material = new THREE.PointsMaterial({{color: 0xffffff, size: 0.02}});
    const particlesMesh = new THREE.Points(geometry, material);
    scene.add(particlesMesh);

    function colorParticles(mood) {{
      const colors = {{
        "😊": 0xffcc66,
        "😢": 0x66aaff,
        "😡": 0xff5555,
        "😴": 0x9999cc,
        "😎": 0x33e0cc
      }};
      material.color.setHex(colors[mood] || 0xffffff);
    }}

    function animate(){{ 
      requestAnimationFrame(animate);
      particlesMesh.rotation.y += 0.0009;
      particlesMesh.rotation.x += 0.0004;
      renderer.render(scene, camera);
    }}
    animate();

    window.addEventListener('resize', () => {{
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
    }});
  </script>
</body>
</html>
"""

def run():
    print(f"Serving on port {PORT}...")
    HTTPServer(("", PORT), MyHandler).serve_forever()

if __name__ == "__main__":
    run()