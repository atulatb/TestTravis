# encoding: UTF-8
require 'calabash-android/abase'

class TestDemo < Calabash::ABase

  # button Calabash
  # trait : default definition
  def trait
    "Button marked:'Test'"
  end

  # button of article what return from search API
  def tap_button_test
    tap_when_element_exists(trait, timeout: 36)
    print "TestDemo \n"
  end
end
