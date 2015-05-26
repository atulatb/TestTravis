require 'calabash-android/calabash_steps'
# After Calabash-Android started, Applicaiton run.
#   Calabash will wait for Capture Screen asise
#     and button Calabash can query.
#   Afterward, Calabash_android perform click onto button Calabash 
Given(/^Click Button tap_button_test$/) do
  @current_page = page(TestDemo).tap_button_test
end

