import os
import sys

def main():
    result = os.system('xcodebuild -scheme "Jenkins-Testing" -destination "platform=iOS Simulator,name=iPhone 8" test -only-testing:"Jenkins-TestingUITests/Jenkins_TestingUITests/testExample"')
    print(result)

if __name__== "__main__":
    main()