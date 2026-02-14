import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SimplifierReplyComponent } from './simplifier-reply.component';

describe('SimplifierReplyComponent', () => {
  let component: SimplifierReplyComponent;
  let fixture: ComponentFixture<SimplifierReplyComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SimplifierReplyComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SimplifierReplyComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
