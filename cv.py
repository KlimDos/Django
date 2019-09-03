import cv2

c = cv2.VideoCapture(0)
#gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

while(1):
  _,f = c.read()
  

  #f2 = cv2.GaussianBlur(f, (51, 51), 0)
  #f2 = cv2.rectangle(f, (2600, 800), (4100, 2400), (0, 255, 255), 10)
  f2 = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
  cv2.imshow('Camera Orange Pi',f2)
  k = cv2.waitKey(5)
  if k==1048603:
      #Esc key to stop, or 27 depending your keyboard
      #Touche ESC appuyee. le code peut dependre du clavier. Normalement 27
      break
  elif k==-1:
      continue
  #uncomment to know the code of of the key pressed
  #Decommenter pour connaitre le code de la touche pressee 
  #else:
      #print k 

cv2.destroyAllWindows()
