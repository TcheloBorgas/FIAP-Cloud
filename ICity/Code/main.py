#━━━━━━━━━❮Bibliotecas❯━━━━━━━━━
import cv2
#━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━

#━━━━━━━━━❮Upload❯━━━━━━━━━
video ='Doom Eternal 2021.12.10 - 17.58.51.02.mp4'
cap =cv2.VideoCapture(video)

if __name__ =='__main__':
    
    baly =cv2.imread('Screenshot 2022-08-30 190221.png')
    box =cv2.selectROI('select roi', baly, fromCenter=False)
    print(box)
    
    #zona de pericia --> (45, 14, 517, 245)
    
    tracker = cv2.TrackerCSRT_create()
    tracker.init(baly, box)
    
    
    while cap.isOpened():
        ret, frame =cap.read()
        
        if not ret:
            break
        ok, box =tracker.update(frame)
        
        if ok:
            pt =box[0], box[1]
            pt2 =((box[0] +box[2]), box[1] +box[3])
            cv2.rectangle(frame, pt, pt2, (255, 0, 0), 2, 1)
        
        else:
            print('Falhou')  
        
        cv2.imshow('tracking', frame)
        
        if cv2.waitKey(1) ==27:
            break
    cv2.destroyAllWindows()