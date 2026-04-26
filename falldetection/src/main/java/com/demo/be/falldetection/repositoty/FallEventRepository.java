package com.demo.be.falldetection.repositoty;

import com.demo.be.falldetection.entity.FallEvent;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface FallEventRepository extends JpaRepository<FallEvent, Long> {
}
