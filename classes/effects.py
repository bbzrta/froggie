def typewriter(message,delay=0.01):
  for character in message:
    print(character,end="")
    time.sleep(delay)
  print("")