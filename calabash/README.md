# How to use

### Install Calasbash Android
Please check Document at [Calabash Android](https://github.com/calabash/calabash-android#documentation)

### auto-test with Calahas-Android
1. open terminal
2. move to folder **calabash**
3. copy android APK file to from folder **bin** to folder **calabash**
4. run command
```
calabash-android run NikkeiDive.apk
```
*Note*
* Change APK file name if need
* Resign key if need by command that is output of above command

### Source code Structure
```
/calabash/
|--features/
|--|--step_definitions/
|--|--|--calabash_steps.rb => calabash check my_first.feature and refer here to check
|--|--|--capture_screen.rb => consist of script for click button dummy and result in Capture Screen
|--|--|--detail_screen.rb => consist of script for click button Text in Detail Screen to prove in Detail Screen
|--|--support/ => auto generate by calabash. current, we don't need to care this.
|--|--my_first.feature => define scenario and step by step for testing
```
