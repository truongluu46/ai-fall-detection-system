package com.demo.be.falldetection.service;

import com.demo.be.falldetection.entity.FallEvent;
import com.demo.be.falldetection.entity.User;
import com.demo.be.falldetection.repositoty.FallEventRepository;
import com.demo.be.falldetection.repositoty.UserRepository;
import lombok.*;
import lombok.experimental.FieldDefaults;
import org.springframework.messaging.simp.SimpMessageHeaderAccessor;
import org.springframework.messaging.simp.SimpMessagingTemplate;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;

@Service
@Builder
@RequiredArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE, makeFinal = true)
public class FallEventService {
     FallEventRepository fallEventRepository;
     UserRepository userRepository;
 //  SimpMessagingTemplate messagingTemplate;

     public void handleFall(String status, String username) {
         User user = userRepository.findByUsername(username);

         FallEvent event = new FallEvent();
         event.setStatus(status);
         event.setTimestamp(LocalDateTime.now());
         event.setUser(user);
         fallEventRepository.save(event);
     }
}
