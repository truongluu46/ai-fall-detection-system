import EventCard from '@/components/molecules/event-card';
import type { FallEvent } from '@/types/fall-event';

interface EventListProps {
  events: FallEvent[];
}

export default function EventList({ events }: EventListProps) {
  return (
    <section className="grid gap-4">
      {events.map((event) => (
        <EventCard key={event.id} event={event} />
      ))}
    </section>
  );
}
