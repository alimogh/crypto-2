import WebSocket as WebSocket

url='wss://ws-api.kucoin.com/endpoint'
token= '2neAiuYvAU61ZDXANAGAsiL4-iAExhsBXZxftpOeh_55i3Ysy2q2LEsEWU64mdzUOPusi34M_wGoSf7iNyEWJ2DUBJg2Qp2YGPtw3zSoNQJ9ZoHCVYOuv9iYB9J6i9GjsxUuhPw3BlrzazF6ghq4L_Rsl7OjYVWmP4lDtXlKRyI=.UM7edBGHyOojadyEtaiK_Q==''
socket = WebSocket(url+token)
socket.