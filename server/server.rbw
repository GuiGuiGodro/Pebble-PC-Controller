require 'sinatra'

configure do
  set :port, 5000
  set :bind, '0.0.0.0'
end

post '/data' do
  puts params['button']
  status 200

  puts Dir.pwd
  case params['button'].to_i
  when 0
    system('wscript C:\Users\Richard\Documents\Work\Code\pebble-controller-master\server\handlers\back.vbs')
  when 1
    system('wscript C:\Users\Richard\Documents\Work\Code\pebble-controller-master\server\handlers\up.vbs')
  when 2
    system('wscript C:\Users\Richard\Documents\Work\Code\pebble-controller-master\server\handlers\select.vbs')
  when 3
    system('wscript C:\Users\Richard\Documents\Work\Code\pebble-controller-master\server\handlers\down.vbs')
  end
end