export type FallEventStatus = 'new' | 'reviewed' | 'false_alarm' | 'confirmed';

export interface FallEvent {
  id: number;
  cameraName: string;
  eventTime: string;
  confidenceScore: number;
  status: FallEventStatus;
  note: string;
}
