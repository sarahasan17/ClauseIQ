import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SimplifierComponent } from './simplifier.component';

describe('SimplifierComponent', () => {
  let component: SimplifierComponent;
  let fixture: ComponentFixture<SimplifierComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SimplifierComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SimplifierComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
