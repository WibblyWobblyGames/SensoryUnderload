import pygame, pygame.event, string, random, os, pygame.mixer
from pygame.locals import *

answers = ["valuable", "cause", "banner", "legacy", "research", "information", "empire", "vanquished enemie", "money", "art", "music", "gratitude", "charity", "statue", "inspiration", "friendship", "kindness", "family", "love", "children", "kid", "questions", "debt", "worries", "worry", "relationships", "positivity", "negativity", "responsibility", "bitterness", "trust", "regret", "regret", "yearning", "work", "undesire", "interest", "passion", "loneliness", "lonely", "original", "originality", "demeanor", "good spelling", "people", "parent", "dread", "death", "greatness", "ghost", "gear", "building", "buildings", "heart", "home", "joke", "arcitecture", "sarcasm", "film", "video game", "movie", "writing", "poem", "rap", "voice", "sing", "singing", "reference game", "reference", "loved", "cooking", "baking", "career", "accomplishment", "nothing", "everything", "myself", "body", "melancholy", "sadness", "fame", "fortune", "humanity", "work"]
nouns = ["my ", "a ", "the ", "being "]
all_possible_answers = []
global tracksPlaying
global currentSounds
tracksPlaying = []
currentSounds = []

def generate_possible_answers():
  global answers
  global all_possible_answers
  global nouns
  plural = "s"
  plural_list = [s + plural for s in answers]
  #print plural_list
  noun_combo = [noun + answer for noun in nouns for answer in answers]
  #print noun_combo
  all_possible_answers =  noun_combo + plural_list + answers
  #print all_possible_answers

def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass

def play_track(trackNumber):
  global currentSounds
  global tracksPlaying
  filename = "SensoryUnderload/InBFlat" + trackNumber + ".ogg"
  abspath = os.path.abspath(filename)
  #print "I am your file name, yo " + filename  
  sound = pygame.mixer.Sound(abspath)
  tracksPlaying.append(trackNumber)
  if trackNumber == "20":
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play(0)
  else:
    sound.play(-1)
    currentSounds.append(sound)  

def add_music():
  randomTrackNumber = random.randint(1,19)
  while randomTrackNumber in tracksPlaying:
    randomTrackNumber = random.randint(1,19)
  #print str(randomTrackNumber) + " this is the track number."
  play_track(str(randomTrackNumber))
  print tracksPlaying
  print currentSounds
  
def end_music():
  global tracksPlaying
  global currentSounds  
  for sound in currentSounds:
    sound.stop()
  tracksPlaying = []
  currentSounds = []

def is_answer(answer):
  matches = 0
  print answer + " ANSWER IS HERE."
  continueString = 1
  for word in all_possible_answers:
    #print(word + " AM YOUR WORD " , answer)
    #print word is answer
    if word == answer:
      matches = 1
      #print "FOUND BITCH"
      end_music()
      play_track(str(20))
    elif word.startswith(answer):
      matches = 1
      add_music()
      break
  if not matches:  
    end_music() 
    continueString = 0
  return continueString

def handle_input(inkey, current_string):
  if inkey == K_BACKSPACE:
      current_string = current_string[0:-1]
  elif inkey == K_MINUS:
    current_string.append("_")
  elif inkey <= 127:
    current_string.append(chr(inkey))
    answer = string.join(current_string,"")
    if not is_answer(answer):
      current_string = []
  return current_string

def get_input():
  current_string = []
  generate_possible_answers()
  global tracksPlaying
  while 1:
    inkey = get_key()
    if inkey == K_RETURN:
      return 1    
    if len(tracksPlaying) == 1 and tracksPlaying[0] == "20":
      if not pygame.mixer.music.get_busy():
        #print "done"
        current_string = []
        end_music()       
        current_string = handle_input(inkey,current_string)
      continue
    else: 
        current_string = handle_input(inkey,current_string)
    
def main():
    #print "start"
    pygame.init()
    #pygame.mixer.init()
    size = width, height = 320, 240
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('What Will You Leave Behind?')    
    while 1:
      done = get_input()
      if done:
        break

main()