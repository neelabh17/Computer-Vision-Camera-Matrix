# import cv2
# import numpy as np

# # Make empty black image
# image=np.zeros((20,40,3),np.uint8)

# # Make one pixel red
# image[10,5]=[0,0,255]

# # Save
# cv2.imwrite("result.png",image)

import cv2
cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
print(cap.get(3))
print(cap.get(4))
while(cap.isOpened()):
	ret, frame=cap.read()
	if(ret):
		cv2.imshow("Frmed",frame)
		if(cv2.waitKey(1) & 0xFF==ord('s')):
			cap.release()
			newFile=open("capture_Index.txt","r+")
			k=int(newFile.read(1))
			
			k+=1
			newFile.seek(0)
			newFile.write(str(k))
			newFile.close()
			# text=input("Enter the name of the newFile")
			cv2.imwrite("capture"+str(k)+".jpg",frame)
			print(frame.shape)
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            i=0
            while(i<720):

                i*=10
                j=0
                while(j<1280):
                    gray[i][j]=frame[i][j]
                    j+=1
            cv2.imwrite("psyco.jpg",gray)
			print(gray,"Here im giving shape of the grey image", gray.shape)
			newfr=frame.reshape((720*1280*3,1))
			print(newfr,newfr.shape,newfr)
			
			break

			
	else:
		break
cap.release()
cap.destroyAllWindows()