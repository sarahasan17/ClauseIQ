import { Component, EventEmitter, Output } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { SimplifierService } from '../../services/clause-simplifier.service';

@Component({
  selector: 'app-simplifier',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './simplifier.component.html',
  styleUrls: ['./simplifier.component.css']
})
export class SimplifierComponent {
  userInput: string = '';
  isLoading: boolean = false; // Add isLoading state

  @Output() inputSubmitted = new EventEmitter<string>();
  
  constructor(private simplifierService: SimplifierService) {}

 submitText() {
  if (this.userInput.trim()) {
    this.isLoading = true; // Start loader
    this.simplifierService.simplifyText(this.userInput).subscribe(
      (response) => {
        try {
          // If response is a string, parse it
          const parsedResponse = typeof response === "string" ? JSON.parse(response) : response;

          // Extract the HTML body content
          if (parsedResponse?.simplified_text?.body) {
            this.inputSubmitted.emit(parsedResponse.simplified_text.body);
          } else {
            console.error("Error: Unexpected response format", parsedResponse);
          }

          this.userInput = ''; // Clear input field after submission
          console.log("Simplified text received:", parsedResponse.simplified_text.body);
        } catch (error) {
          console.error("Error parsing response:", error);
        }
        this.isLoading = false; // Stop loader
      },
      (error) => {
        console.error("Error in API call:", error);
        this.isLoading = false; // Stop loader on error
      }
    );
  }
}
}
