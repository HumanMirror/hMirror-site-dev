import webapp2


application = webapp2.WSGIApplication([

  (r'/user/loginnStatus',UserLoginStatus),
  (r'/user/logsIn',UserLogsIn),
  (r'/user/logsOut',UserLogsOut),
  (r'/user/registers',UserRegisters),
  (r'/user/votes',UserVotesAnAudio),
  
],config=config, debug=False)