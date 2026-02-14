import { bootstrapApplication } from '@angular/platform-browser';
import { importProvidersFrom } from '@angular/core';
import { provideHttpClient } from '@angular/common/http'; // ✅ Import HttpClient provider
import { provideRouter } from '@angular/router';
import { AppComponent } from './app/app.component';

bootstrapApplication(AppComponent, {
  providers: [
    provideHttpClient(), // ✅ Correct way to provide HttpClient in standalone mode
    provideRouter([]),
  ],
}).catch((err) => console.error(err));
