// App Component (app.component.ts)
import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { FileFormComponent } from './MyComponents/file-form/file-form.component';
import { CommonModule } from '@angular/common';
import { DomSanitizer, SafeResourceUrl } from '@angular/platform-browser';
import { SummarizerComponent } from './MyComponents/summarizer/summarizer.component';
import { SimplifierComponent } from './MyComponents/simplifier/simplifier.component';
import { NavbarComponent } from './MyComponents/navbar/navbar.component';
import { SimplifierReplyComponent } from './MyComponents/simplifier-reply/simplifier-reply.component';
import * as pdfjsLib from 'pdfjs-dist';
import { SummarizerService } from './services/summarizer.service';
import { HttpClient } from '@angular/common/http';

pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/4.10.38/pdf.worker.min.mjs';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [ FileFormComponent, CommonModule, SummarizerComponent, SimplifierComponent, NavbarComponent, SimplifierReplyComponent],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  pdfURL: SafeResourceUrl | null = null;
  extractedText: string = ''; // Holds extracted text
  replyText: string = ''; // Holds processed text
  isLoading: boolean = false; // Loader state
  isDivVisible: boolean = false;

  constructor(private sanitizer: DomSanitizer, private summarizerService: SummarizerService) {}

async onFileSelected(file: File) {
  console.log('Received file in AppComponent:', file.name);
  this.isLoading = true; // Start loader

  this.summarizerService.summarizeFile(file).subscribe(
    (response) => {
      this.extractedText = response; 
      console.log('Summary received:', response);
      this.isLoading = false; // Stop loader
      this.isDivVisible = true;
    },
    (error) => {
      console.error('Error sending file:', error);
      this.isLoading = false; // Stop loader on error
    }
  );

  // Load the PDF into the UI
  const unsafeURL = URL.createObjectURL(file);
  this.pdfURL = this.sanitizer.bypassSecurityTrustResourceUrl(unsafeURL);
}

  handleInput(input: string) {
    this.replyText = input; // Update text for ReplyBoxComponent
  }
}
