'use client'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faUser } from '@fortawesome/free-regular-svg-icons'
import { faChevronDown } from '@fortawesome/free-solid-svg-icons'
import { useAnimate } from 'framer-motion'
import { cn } from '@/utils/tw'
import { useState } from 'react'

export const SideBarNavDrawer = () => {
  const [scope, animate] = useAnimate()
  const [isOpen, setIsOpen] = useState<boolean>(false)

  const toggleDrawer = () => {
    if (!isOpen) {
      animate('#drawer', { height: 'auto' }, { duration: 0.3 })
      animate('#chev', { rotate: 180 }, { duration: 0.3 })
    }
    if (isOpen) {
      animate('#drawer', { height: '0' }, { duration: 0.3 })
      animate('#chev', { rotate: 0 }, { duration: 0.3 })
    }
    setIsOpen(!isOpen)
  }

  return (
    <div ref={scope}>
      <div
        className="flex p-3 w-full gap-2 items-center rounded-lg text-white cursor-pointer bg-primary "
        onClick={() => toggleDrawer()}
      >
        <FontAwesomeIcon icon={faUser} className="w-4 h-4" /> <p>Dashboard</p>
        <FontAwesomeIcon
          icon={faChevronDown}
          className="ml-auto w-4 h-4"
          id="chev"
        />
      </div>

      {/* drawer */}
      <div
        className="pt-3 px-4 overflow-hidden"
        style={{ height: 0 }}
        id="drawer"
      >
        <div className="border-l-2 px-2">
          <SideBarItem
            name={`Accounts`}
            icon={
              <FontAwesomeIcon icon={faUser} className="w-[1rem] h-[1rem]" />
            }
          />
        </div>
        <div className="border-l-2 px-2">
          <SideBarItem
            name={`Accounts`}
            icon={
              <FontAwesomeIcon icon={faUser} className="w-[1rem] h-[1rem]" />
            }
          />
        </div>
        <div className="border-l-2 px-2">
          <SideBarItem
            name={`Accounts`}
            icon={
              <FontAwesomeIcon icon={faUser} className="w-[1rem] h-[1rem]" />
            }
          />
        </div>
      </div>
    </div>
  )
}

export type SideBarItemProps = {
  name: string
  icon: React.ReactNode
  isActive?: boolean
}

export const SideBarItem = ({
  name,
  icon,
  isActive = false,
}: SideBarItemProps) => {
  return (
    <div
      className={cn(
        'flex p-3 w-full gap-2 items-center rounded-lg text-text-muted cursor-pointer transition-colors',
        isActive ? 'bg-primary-accent text-primary' : ''
      )}
    >
      {icon}
      {name}
    </div>
  )
}
