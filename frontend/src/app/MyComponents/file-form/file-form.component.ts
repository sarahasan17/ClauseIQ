import { Component, EventEmitter, Output } from '@angular/core';
import { CommonModule } from '@angular/common';
@Component({
  selector: 'app-file-form',
  imports: [CommonModule],
  templateUrl: './file-form.component.html',
  styleUrl: './file-form.component.css'
})
export class FileFormComponent {
  fileName: string | null = null;
  errorMessage: string | null = null;
  @Output() fileSelected = new EventEmitter<File>();

  onFileSelected(event: Event) {
    const input = event.target as HTMLInputElement;
    this.errorMessage = null;
    if (input.files && input.files.length > 0) {
      const selectedFile = input.files[0];

       // Validate file type (only allow PDFs)
      if (selectedFile.type !== 'application/pdf') {
        this.errorMessage = 'Invalid file type. Please select a PDF.';
        console.warn(this.errorMessage);
        alert("Invalid file type. Please select a PDF.");
        return;
      }


      this.fileName = selectedFile.name;
      console.log('File Selected:', selectedFile.name, selectedFile);

      this.fileSelected.emit(selectedFile); // Emit event to parent
    } else {
      console.warn('No file selected.');
    }
  }
}
