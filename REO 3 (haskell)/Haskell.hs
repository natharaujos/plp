statistics :: String -> (String, Int)
statistics txt = ([head txt, '.', last txt], length txt)


