import React, { useState } from 'react';
import { TextField, Button, Container, Box, Typography, Paper } from '@mui/material';
import { Send as SendIcon } from '@mui/icons-material';

const ChatboxPage = () => {
  const [messages, setMessages] = useState([
    { sender: 'chatgpt', message: 'Hello! How can I assist you today?' }
  ]);
  const [userMessage, setUserMessage] = useState('');

  const handleMessageSubmit = (e) => {
    e.preventDefault();
    if (userMessage.trim() !== '') {
      setMessages([
        ...messages,
        { sender: 'user', message: userMessage },
        { sender: 'chatgpt', message: 'Let me help you with that!' } // Sample response from ChatGPT
      ]);
      setUserMessage('');
    }
  };

  return (
    <Container maxWidth="sm" sx={{ mt: 5 }}>
      <Paper elevation={3} sx={{ padding: 2 }}>
        <Box display="flex" flexDirection="column" height="70vh">
          {/* Chat Header */}
          <Box mb={2}>
            <Typography variant="h5" component="h2" align="center">
              Snort Rule Configurator Chat
            </Typography>
            <Typography variant="body2" color="textSecondary" align="center">
              Get your Snort rule configurations generated!
            </Typography>
          </Box>

          {/* Messages Section */}
          <Box 
            sx={{
              flexGrow: 1,
              overflowY: 'auto',
              marginBottom: 2,
              padding: 1,
              backgroundColor: '#f9f9f9',
              borderRadius: 1,
            }}
          >
            {messages.map((msg, index) => (
              <Box
                key={index}
                sx={{
                  display: 'flex',
                  justifyContent: msg.sender === 'user' ? 'flex-end' : 'flex-start',
                  mb: 1,
                }}
              >
                <Box
                  sx={{
                    maxWidth: '70%',
                    padding: 1.5,
                    borderRadius: 2,
                    bgcolor: msg.sender === 'user' ? '#007bff' : '#e5e5e5',
                    color: msg.sender === 'user' ? 'white' : 'black',
                    wordWrap: 'break-word',
                  }}
                >
                  {msg.message}
                </Box>
              </Box>
            ))}
          </Box>

          {/* User Input */}
          <Box component="form" onSubmit={handleMessageSubmit} display="flex">
            <TextField
              variant="outlined"
              fullWidth
              value={userMessage}
              onChange={(e) => setUserMessage(e.target.value)}
              placeholder="Type your message..."
              sx={{ mr: 2 }}
            />
            <Button 
              type="submit" 
              variant="contained" 
              color="primary" 
              sx={{ height: '100%' }}
              startIcon={<SendIcon />}
            >
              Send
            </Button>
          </Box>
        </Box>
      </Paper>
    </Container>
  );
};

export default ChatboxPage;
