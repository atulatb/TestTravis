# encoding: UTF-8
require 'calabash-android/abase'

class DetailScreen < Calabash::ABase

  # button Text
  # trait : default definition
  def trait
    "Button marked:'Text'"
  end

  # wait detail screnn appear when Calabash-Android click button of result article
  def wait_detail_screen
    print "wait detail screen \n"
    sleep(10)
    wait_for_elements_exist(trait, timeout: 60)
    print "in detail screen \n"
    self
  end
  
  # Calabash-Android perform click event onto button Text 
  #   to check application being in Detail Screen
  def tap_button_text
    print "Click button Text \n"
    tap_when_element_exists(trait, timeout: 60)
    print "Clicked button Text \n"
  end
end
