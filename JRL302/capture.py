import cv2
cap=cv2.VideoCapture(1)
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
			cv2.imwrite("psyco.jpg",gray)
			op=cv2.imread("psyco.jpg")
			print(op.shape)
			i=0
			while(i<719):
				print(i)
				
				j=0
				while(j<1280):
					op[i,j]=[frame[i,j][0],frame[i,j][1],frame[i,j][2]]
					op[i+1,j]=[frame[i+1,j][0],frame[i+1,j][1],frame[i+1,j][2]]
					j+=1
				i+=15
			i=0
			while(i<718):
				print(i)
				
				j=0
				while(j<1280):
					op[i,j]=[frame[i,j][0],frame[i,j][1],frame[i,j][2]]
					op[i+1,j]=[frame[i+1,j][0],frame[i+1,j][1],frame[i+1,j][2]]
					op[i+2,j]=[frame[i+2,j][0],frame[i+2,j][1],frame[i+2,j][2]]
					j+=15
				i+=1
			cv2.imwrite("op.jpg",op)
			print(gray,"Here im giving shape of the grey image", gray.shape)
			newfr=frame.reshape((720*1280*3,1))
			print(newfr,newfr.shape,newfr)
			
			break

			
	else:
		break
cap.release()
cap.destroyAllWindows()