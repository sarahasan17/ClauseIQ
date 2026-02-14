import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';


@Component({
  selector: 'app-summarizer',
  imports: [CommonModule],
  templateUrl: './summarizer.component.html',
  styleUrl: './summarizer.component.css'
})
export class SummarizerComponent {
 @Input() extractedText: string = ''; // Receives text from AppComponent // Currently taking text from app component, but it should take the text from backend
}
