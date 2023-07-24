from deepface import DeepFace


result = DeepFace.verify(img1_path = "13_face_verification/image1.jpg", 
                         img2_path = "13_face_verification/image2.jpg", 
                         model_name = "ArcFace")
print(result)
