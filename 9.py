def brute_force_otp(real_otp):
    print("Starting brute-force simulation...\n")
    for guess in range(10000): 
        attempt = str(guess).zfill(4)  
        print("Trying:", attempt)
        if attempt == real_otp:
            print(" OTP matched:", attempt)
            return
    print(" OTP not found.")


brute_force_otp("9226")