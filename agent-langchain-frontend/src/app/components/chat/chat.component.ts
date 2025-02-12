import { Component, OnInit } from '@angular/core';
import axios from 'axios';

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.scss']
})
export class ChatComponent implements OnInit {
  userMessage: string = '';
  chatHistory: { user: string, bot: string }[] = [];

  constructor() {}

  ngOnInit(): void {}

  async sendMessage() {
    if (!this.userMessage.trim()) return;

    const userMessage = this.userMessage;
    this.chatHistory.push({ user: userMessage, bot: "..." });

    try {
      const response = await axios.post('http://127.0.0.1:8000/chat', { message: userMessage });
      this.chatHistory[this.chatHistory.length - 1].bot = response.data.response;
    } catch (error) {
      console.error("Error fetching response:", error);
    }

    this.userMessage = '';
  }
}
